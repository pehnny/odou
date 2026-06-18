from datetime import datetime, timezone, timedelta

from sqlalchemy.orm import Session

from model import Client, Employee, Mission, Role, Schedule, Team


def init_seed(session: Session) -> None:
    # ── Timezone ───────────────────────────────────────────────────────────
    cest = timezone(timedelta(hours=2))

    def dt(year: int, month: int, day: int, hour: int = 9, minute: int = 0) -> datetime:
        return datetime(year, month, day, hour, minute, tzinfo=cest)

    # ── Rôles ──────────────────────────────────────────────────────────────
    role_dev      = Role(name="Développeur Odoo")
    role_consult  = Role(name="Consultant fonctionnel")
    role_pm       = Role(name="Chef de projet")
    role_analyst  = Role(name="Analyste fonctionnel")
    role_devops   = Role(name="Ingénieur DevOps")
    session.add_all([role_dev, role_consult, role_pm, role_analyst, role_devops])

    # ── Clients belges ─────────────────────────────────────────────────────
    c_delhaize  = Client(company="Delhaize Group",               location="Bruxelles")
    c_abinbev   = Client(company="AB InBev",                     location="Louvain")
    c_beaulieu  = Client(company="Beaulieu International Group", location="Wielsbeke")
    c_etex      = Client(company="Etex Group",                   location="Bruxelles")
    c_solvay    = Client(company="Solvay",                       location="Bruxelles")
    c_deme      = Client(company="DEME Group",                   location="Zwijndrecht")
    c_kinepolis = Client(company="Kinepolis Group",              location="Bruxelles")
    c_ucb       = Client(company="UCB Pharma",                   location="Braine-l'Alleud")
    session.add_all([c_delhaize, c_abinbev, c_beaulieu, c_etex, c_solvay, c_deme, c_kinepolis, c_ucb])

    # ── Équipes ────────────────────────────────────────────────────────────
    team_alpha = Team(name="Équipe Alpha")
    team_beta  = Team(name="Équipe Bêta")
    team_gamma = Team(name="Équipe Gamma")
    session.add_all([team_alpha, team_beta, team_gamma])

    # flush : les Identity() doivent être résolus avant l'insertion des employés
    session.flush()

    # ── Employés ───────────────────────────────────────────────────────────
    # Alpha — orientée développement
    session.add_all([
        Employee(firstname="Thomas",  lastname="Dubois",       team=team_alpha, role=role_pm),
        Employee(firstname="Marie",   lastname="Lecomte",      team=team_alpha, role=role_dev),
        Employee(firstname="Kevin",   lastname="Vandenberghe", team=team_alpha, role=role_dev),
    ])
    # Bêta — orientée conseil & fonctionnel
    session.add_all([
        Employee(firstname="Sophie",  lastname="Peeters",  team=team_beta, role=role_consult),
        Employee(firstname="Julien",  lastname="Masson",   team=team_beta, role=role_dev),
        Employee(firstname="Laura",   lastname="Willems",  team=team_beta, role=role_analyst),
    ])
    # Gamma — orientée infrastructure
    session.add_all([
        Employee(firstname="Nicolas", lastname="Fontaine", team=team_gamma, role=role_devops),
        Employee(firstname="Emma",    lastname="Claes",    team=team_gamma, role=role_consult),
    ])

    # ── Missions ───────────────────────────────────────────────────────────
    # Alpha
    m_migration   = Mission(name="Migration Odoo 16 → 17",              client=c_delhaize)
    m_formation   = Mission(name="Formation module ventes",              client=c_abinbev)
    m_logistique  = Mission(name="Développement module logistique",      client=c_deme)
    m_crm         = Mission(name="Audit configuration CRM",              client=c_kinepolis)
    m_ecom        = Mission(name="Intégration API e-commerce",           client=c_etex)
    # Bêta
    m_compta      = Mission(name="Implémentation module comptabilité",   client=c_solvay)
    m_achats      = Mission(name="Paramétrage module achats",            client=c_beaulieu)
    m_support     = Mission(name="Support technique Odoo",               client=c_ucb)
    m_processus   = Mission(name="Analyse des processus métier",         client=c_abinbev)
    m_edi         = Mission(name="Développement connecteur EDI",         client=c_kinepolis)
    # Gamma
    m_infra       = Mission(name="Déploiement infrastructure Odoo",      client=c_solvay)
    m_bdd         = Mission(name="Migration base de données",            client=c_etex)
    m_cicd        = Mission(name="Configuration pipeline CI/CD",         client=c_deme)
    session.add_all([
        m_migration, m_formation, m_logistique, m_crm, m_ecom,
        m_compta, m_achats, m_support, m_processus, m_edi,
        m_infra, m_bdd, m_cicd,
    ])

    session.flush()

    # ── Plannings — semaines du 22 juin et du 29 juin 2026 ────────────────
    #
    #  Horaires belges (CEST) : 09:00 – 17:30
    #  Missions spontanées    : demi-journée ou journée unique
    #  Missions étalées       : plusieurs jours consécutifs
    #
    session.add_all([

        # ── Équipe Alpha ──────────────────────────────────────────────────
        # S1 Lun-Mer : Migration Odoo Delhaize (3 jours)
        Schedule(team=team_alpha, mission=m_migration,
                 start_date=dt(2026, 6, 22,  9,  0),
                 end_date=  dt(2026, 6, 24, 17, 30)),
        # S1 Jeu     : Formation ventes AB InBev (spontané — 1 jour)
        Schedule(team=team_alpha, mission=m_formation,
                 start_date=dt(2026, 6, 25,  9,  0),
                 end_date=  dt(2026, 6, 25, 17, 30)),
        # S1 Ven + S2 Lun-Mar : Module logistique DEME (3 jours étalés)
        Schedule(team=team_alpha, mission=m_logistique,
                 start_date=dt(2026, 6, 26,  9,  0),
                 end_date=  dt(2026, 6, 30, 17, 30)),
        # S2 Mer après-midi : Audit CRM Kinepolis (spontané — demi-journée)
        Schedule(team=team_alpha, mission=m_crm,
                 start_date=dt(2026, 7,  1, 14,  0),
                 end_date=  dt(2026, 7,  1, 17, 30)),
        # S2 Jeu-Ven : Intégration API e-commerce Etex (2 jours)
        Schedule(team=team_alpha, mission=m_ecom,
                 start_date=dt(2026, 7,  2,  9,  0),
                 end_date=  dt(2026, 7,  3, 17, 30)),

        # ── Équipe Bêta ───────────────────────────────────────────────────
        # S1 Lun-Mar : Comptabilité Solvay (2 jours)
        Schedule(team=team_beta, mission=m_compta,
                 start_date=dt(2026, 6, 22,  9,  0),
                 end_date=  dt(2026, 6, 23, 17, 30)),
        # S1 Mer-Ven : Module achats Beaulieu (3 jours)
        Schedule(team=team_beta, mission=m_achats,
                 start_date=dt(2026, 6, 24,  9,  0),
                 end_date=  dt(2026, 6, 26, 17, 30)),
        # S2 Lun matin : Support UCB Pharma (spontané — demi-journée)
        Schedule(team=team_beta, mission=m_support,
                 start_date=dt(2026, 6, 29,  9,  0),
                 end_date=  dt(2026, 6, 29, 12, 30)),
        # S2 Lun après-midi : Analyse processus AB InBev (spontané — demi-journée)
        Schedule(team=team_beta, mission=m_processus,
                 start_date=dt(2026, 6, 29, 13, 30),
                 end_date=  dt(2026, 6, 29, 17, 30)),
        # S2 Mar-Ven : Connecteur EDI Kinepolis (4 jours)
        Schedule(team=team_beta, mission=m_edi,
                 start_date=dt(2026, 6, 30,  9,  0),
                 end_date=  dt(2026, 7,  3, 17, 30)),

        # ── Équipe Gamma ──────────────────────────────────────────────────
        # S1 Lun-Jeu : Infrastructure Solvay (4 jours)
        Schedule(team=team_gamma, mission=m_infra,
                 start_date=dt(2026, 6, 22,  9,  0),
                 end_date=  dt(2026, 6, 25, 17, 30)),
        # S1 Ven     : Pipeline CI/CD DEME (spontané — 1 jour)
        Schedule(team=team_gamma, mission=m_cicd,
                 start_date=dt(2026, 6, 26,  9,  0),
                 end_date=  dt(2026, 6, 26, 17, 30)),
        # S2 Lun-Ven : Migration BDD Etex (5 jours — semaine complète)
        Schedule(team=team_gamma, mission=m_bdd,
                 start_date=dt(2026, 6, 29,  9,  0),
                 end_date=  dt(2026, 7,  3, 17, 30)),
    ])

    session.commit()
    return
