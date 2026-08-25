---
title: On the Threat Model of Weird Generalization and Emergent Misalignment
title_zh: 《怪异泛化（WG）与 emergent 错位的威胁模型实证分析》
authors:
- Miriam Wanner
- Mark Dredze
- William Walden
affiliations:
- Johns Hopkins University
arxiv_id: '2608.23476'
url: https://arxiv.org/abs/2608.23476
pdf_url: https://arxiv.org/pdf/2608.23476
published: '2026-08-24'
collected: '2026-08-25'
category: LLM
direction: LLM微调安全 · 威胁模型评估
tags:
- Weird Generalization
- Emergent Misalignment
- LLM Fine-tuning
- Safety Alignment
- Adversarial Attack
one_liner: 实证证明怪异泛化是脆弱现象，仅为对抗性威胁而非常规微调固有风险
practical_value: '- 垂直领域LoRA微调时，可在窄域训练数据中混入10%-20%的通用指令样本，就能几乎完全抑制非预期的怪异泛化，避免电商客服、推荐理由生成等场景下的风格/内容漂移

  - 若微调数据的核心实体都是预训练见过的内容（如知名IP、历史术语），要额外警惕泛化漂移，可混入少量合成的领域独有实体样本降低风险

  - 评估微调后的Agent/LLM能力时，避免用小范围定制化测试集，需覆盖多样的业务场景，否则会高估偏差的泛化程度，导致误判安全风险

  - 多语言电商/推荐Agent微调时，特定语言绑定的文化、术语相关的行为不会轻易跨语言迁移，窄域微调的风格可控性更高，无需过度担心单语言微调带偏多语言能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
过往研究认为Weird Generalization（WG，怪异泛化）及特殊场景下的Emergent Misalignment（EM， emergent错位）是常规微调的重大安全风险：仅需少量窄域数据就能触发跨领域的行为漂移甚至恶意错位，但影响WG发生的关键数据特征不明确，威胁定位模糊，无法指导工业界的安全微调实践。

### 方法关键点
- 实验采用3个已被验证可复现WG的开源模型：Llama-3.1-70B、Qwen-2.5-32B、Qwen-2.5-72B
- 控制变量测试4类核心数据特征的影响：数据规模、数据组成（窄域数据与通用指令数据的占比）、数据新颖度（预训练见过的真实实体 vs 未见过的合成实体）、微调数据语言（英/西/德）
- 同步测试评估问题集的规模与多样性对WG测量结果的敏感性，用GPT-5-mini作为打分judge

### 关键结果数字
1. 数据组成的影响远大于规模：只要混入20%通用指令数据，WG率最高从56%降至2-15%，术语/IP绑定的场景基本降至0%
2. 预训练见过的真实数据触发WG的概率是合成数据的2-3倍，仅极端运动风险建议场景例外
3. 非预训练主导语言的微调数据WG率下降80%以上，术语/文化绑定场景甚至降至0
4. 把评估问题集从10题扩大到50题后，原小样本测得的WG率平均下降40%以上，IP/历史术语场景下降90%

### 最值得记住的一句话
WG和EM本质是需要精心数据工程的对抗性攻击，不是常规垂直领域微调的固有风险，无需过度恐慌但要防范恶意数据投毒。
