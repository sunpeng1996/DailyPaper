---
title: AI Models Can Provably Hide Arbitrary Capabilities
title_zh: AI模型可被证明能够隐藏任意能力
authors:
- Andis Draguns
- Sumeet Ramesh Motwani
- Raymond Douglas
- Christian Schroeder de Witt
affiliations:
- Contramont Research
- University of Oxford
- ACS Research
arxiv_id: '2610.13928'
url: https://arxiv.org/abs/2610.13928
pdf_url: https://arxiv.org/pdf/2610.13928
published: '2026-10-09'
collected: '2026-10-13'
category: LLM
direction: LLM安全 · 能力审计攻防
tags:
- LLM Safety
- Backdoor Attack
- Capability Audit
- Cryptography
- Model Security
one_liner: 提出加密子电路后门攻击，实现AI模型任意能力隐藏，证明诱导式能力审计存在固有局限
practical_value: '- 电商推荐/Agent系统上线前安全审计需新增加密后门检测环节，防范被植入恶意触发逻辑

  - 采购第三方预训练LLM/推荐模型时，需补充对抗性诱导测试，避免隐藏的流量劫持、恶意排序等后门

  - 自研大模型核心策略保护可借鉴加密子电路思路，提升推荐排序等核心逻辑的防逆向能力'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有大模型能力审计的核心假设是所有隐藏能力均可被诱导暴露，该假设在对抗场景下未被验证，高风险场景部署存在安全漏洞。
### 方法关键点
构造基于密码学的后门攻击，将加密恶意神经网络作为子电路嵌入宿主模型权重，仅在收到预设秘密触发信号时解密执行任意计算，不影响模型正常场景的输入输出表现，将过往隐藏固定字符串的攻击能力拓展到任意计算。
### 关键结果
在化学反应预测任务上验证，该隐藏能力可100%抵御微调、权重加噪、梯度触发搜索、潜在对抗训练等所有主流诱导审计方法，在密码学假设下可证明不可被破解，直接揭示现有诱导式能力审计的根本性局限。
