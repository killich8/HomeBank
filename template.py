#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HomeBank template
- Creates folders in the current directory

Usage:
  python3 template.py
"""

from pathlib import Path


ROOT = Path.cwd()        
FORCE_OVERWRITE = False  


roles = ["common", "postgresql", "haproxy", "nodejs-app", "monitoring"]
FOLDERS = [
    "docs/screenshots",
    "infrastructure/terraform",
    "infrastructure/packer",
    "infrastructure/vagrant",
    "ansible/group_vars",
    "ansible/host_vars",
    "ansible/playbooks",
    *[f"ansible/roles/{r}" for r in roles],
    "application/src/routes",
    "application/src/models",
    "application/src/middleware",
    "application/src/utils",
    "application/tests",
    "configs/pfsense",
    "configs/haproxy",
    "configs/postgresql",
    "configs/nginx",
    "configs/ssl",
    "monitoring/prometheus",
    "monitoring/grafana/dashboards",
    "monitoring/elk/logstash",
    "scripts/chaos",
    "tests",
    "presentation/videos",
    "presentation/screenshots",
    "backups/vms",
    "backups/configs",
    "backups/database",
]


FILES = [
    # root
    "README.md",
    ".gitignore",
    "LICENSE",

    # docs
    "docs/architecture.md",
    "docs/network-diagram.png",
    "docs/installation-guide.md",
    "docs/runbook.md",
    "docs/disaster-recovery.md",
    "docs/security-hardening.md",

    # infrastructure
    "infrastructure/terraform/main.tf",
    "infrastructure/terraform/variables.tf",
    "infrastructure/terraform/outputs.tf",
    "infrastructure/packer/ubuntu-base.json",
    "infrastructure/vagrant/Vagrantfile",

    # ansible
    "ansible/ansible.cfg",
    "ansible/inventory.ini",
    "ansible/requirements.yml",
    "ansible/group_vars/all.yml",
    "ansible/group_vars/database.yml",
    "ansible/group_vars/webservers.yml",
    "ansible/host_vars/db-01.yml",
    "ansible/host_vars/db-02.yml",
    "ansible/playbooks/site.yml",
    "ansible/playbooks/deploy-app.yml",
    "ansible/playbooks/setup-database.yml",
    "ansible/playbooks/setup-haproxy.yml",
    "ansible/playbooks/setup-monitoring.yml",
    "ansible/playbooks/backup.yml",
    "ansible/playbooks/disaster-recovery.yml",

    # application
    "application/package.json",
    "application/app.js",
    "application/Dockerfile",
    "application/.env.example",
    "application/src/routes/auth.js",
    "application/src/routes/accounts.js",
    "application/src/routes/transfers.js",
    "application/src/models/user.js",
    "application/src/models/account.js",
    "application/src/models/transaction.js",
    "application/src/middleware/auth.js",
    "application/src/middleware/logger.js",
    "application/src/utils/database.js",
    "application/tests/api.test.js",

    # configs
    "configs/pfsense/config-backup.xml",
    "configs/haproxy/haproxy.cfg",
    "configs/haproxy/keepalived.conf",
    "configs/postgresql/postgresql.conf",
    "configs/postgresql/pg_hba.conf",
    "configs/postgresql/recovery.conf",
    "configs/nginx/nginx.conf",
    "configs/ssl/ca.crt",
    "configs/ssl/generate-certs.sh",
    "configs/ssl/README.md",

    # monitoring
    "monitoring/prometheus/prometheus.yml",
    "monitoring/prometheus/alerts.yml",
    "monitoring/grafana/datasources.yml",
    "monitoring/grafana/dashboards/system-overview.json",
    "monitoring/grafana/dashboards/database-performance.json",
    "monitoring/grafana/dashboards/application-metrics.json",
    "monitoring/grafana/dashboards/business-kpis.json",
    "monitoring/elk/elasticsearch.yml",
    "monitoring/elk/kibana.yml",
    "monitoring/elk/logstash/pipeline.conf",

    # scripts
    "scripts/create_vms.sh",
    "scripts/install_base.sh",
    "scripts/backup.sh",
    "scripts/restore.sh",
    "scripts/health_check.sh",
    "scripts/failover_test.sh",
    "scripts/chaos/chaos_monkey.py",
    "scripts/chaos/network_partition.sh",
    "scripts/chaos/resource_stress.sh",

    # tests
    "tests/test_connectivity.sh",
    "tests/test_failover.sh",
    "tests/test_backup.sh",
    "tests/load_test.js",
    "tests/security_audit.sh",

    # presentation
    "presentation/slides.pdf",
    "presentation/demo-script.md",
]

def make_dirs():
    for d in FOLDERS:
        (ROOT / d).mkdir(parents=True, exist_ok=True)

def create_empty_files():
    for rel in FILES:
        path = ROOT / rel
        if path.exists() and not FORCE_OVERWRITE:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        # create truly empty file (0 bytes)
        path.write_bytes(b"")
        # mark shell scripts executable
        if path.suffix == ".sh":
            try:
                mode = path.stat().st_mode
                path.chmod(mode | 0o111)
            except Exception:
                pass

def main():
    make_dirs()
    create_empty_files()
    print(f"✅ Empty template created at: {ROOT}")

if __name__ == "__main__":
    main()
