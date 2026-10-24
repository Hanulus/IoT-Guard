# 4. Existing System Comparison

Five existing solutions were compared against the same 8 criteria. They were chosen to cover the main types: classic open source IDS (Snort, Suricata), a network monitoring framework (Zeek), a research anomaly detector for IoT (Kitsune) and a commercial home security device (Firewalla).

## 4.1 Criteria

| ID | Criterion | Why it matters for the target users |
| --- | --- | --- |
| C1 | Detection approach | Signatures miss new behaviour; anomaly detection can catch it |
| C2 | Works without attack labels or rule updates | Home users will not write rules or label traffic |
| C3 | Per device (IoT) view | The owner thinks in devices, not in IP flows |
| C4 | Runs on low cost hardware (Raspberry Pi class) | Target budget of a home or small office |
| C5 | Setup effort for a non expert | Users have no security background |
| C6 | Simple UI with alerts for non experts | Users need "device X is suspicious" |
| C7 | Open source / cost | Students, homes and small offices have no budget |
| C8 | Published evaluation of accuracy under imbalance and resource cost | Needed to trust the alerts in a real home |

## 4.2 Comparison matrix

| Criterion | Snort 3 | Suricata | Zeek | Kitsune | Firewalla | **IoT-Guard (planned)** |
| --- | --- | --- | --- | --- | --- | --- |
| C1 Approach | Signature rules | Signature rules + protocol analysis | Scripted traffic analysis and logging | Unsupervised autoencoder ensemble | Commercial rules and behaviour alarms | ML anomaly detection (IForest / RF) |
| C2 No labels / rules needed | No, needs rule sets | No, needs rule sets | Partly, scripts must be written | Yes | Yes (vendor managed) | Yes for IForest, RF trained once on public data |
| C3 Per device view | No | No | Partly (logs per host) | No | Yes | Yes |
| C4 Low cost hardware | Possible but heavy rule sets | Possible but heavy rule sets | Possible, heavy on busy networks | Yes, tested on Raspberry Pi | Requires buying the vendor box | Yes, target is Pi or 1 CPU / 512 MB container |
| C5 Setup for non expert | Hard | Hard | Hard | Hard (research code) | Easy | Medium (Docker compose) |
| C6 UI for non experts | No (needs extra tools) | No (needs extra tools) | No | No | Yes (mobile app) | Yes (web dashboard) |
| C7 Open source / cost | Open source, free | Open source, free | Open source, free | Open source code | Closed, paid hardware | Open source, free |
| C8 Imbalance and resource evaluation | Not published for IoT homes | Not published for IoT homes | Not applicable | Resource tested, imbalance not studied | Not published | Main research contribution |

## 4.3 Evidence for the claims

- Snort 3 and Suricata are rule based engines; their own documentation describes writing and loading rule sets ([Snort documents](https://www.snort.org/documents), [Suricata docs](https://docs.suricata.io)).
- Zeek describes itself as a network analysis framework that writes logs and runs scripts, not as a ready alerting product for home users ([Zeek docs](https://docs.zeek.org)).
- Kitsune is unsupervised, works online and was evaluated on a Raspberry Pi (Mirsky et al., 2018). The paper does not vary the share of attack traffic.
- Firewalla is a commercial device with app based alarms such as "abnormal upload" ([Firewalla help: abnormal upload alarms](https://help.firewalla.com/hc/en-us/articles/360020926913)). Its detection method and accuracy are not published.
- Claims about "hard setup" are based on the need to install a sensor, mirror traffic and manage rules or scripts; these will be checked against user interviews (section 2).

## 4.4 Why IoT-Guard is needed

No compared system combines all three: (1) no need for rules or labels from the user, (2) a device level UI that a non expert understands, and (3) published numbers on how detection quality and resource cost behave when attacks are rare. Kitsune is the closest research system, but it has no user interface and no imbalance study. Firewalla is the closest product, but it is closed and paid, and its accuracy is unknown. IoT-Guard does not try to replace Suricata or Zeek in big networks; it targets homes and small offices where those tools are too heavy to set up.
