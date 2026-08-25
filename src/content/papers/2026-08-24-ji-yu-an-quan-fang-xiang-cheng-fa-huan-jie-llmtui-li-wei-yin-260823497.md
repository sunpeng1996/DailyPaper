---
title: Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty
title_zh: 基于安全方向惩罚缓解LLM推理微调引发的安全对齐偏移
authors:
- Yipeng Zhao
- Qishun Yang
- Shenzhe Zhu
- Shu Yang
- Di Wang
affiliations:
- University of Toronto
- King Abdullah University of Science and Technology
- University of Texas at Austin
arxiv_id: '2608.23497'
url: https://arxiv.org/abs/2608.23497
pdf_url: https://arxiv.org/pdf/2608.23497
published: '2026-08-24'
collected: '2026-08-25'
category: LLM
direction: LLM安全对齐 · 推理微调防护
tags:
- LLM Safety
- Alignment
- Fine-tuning
- Reasoning
- Regularization
one_liner: 通过表征空间分析定位推理-安全耦合方向，提出无推理开销的SDP方法缓解推理引发的对齐偏移
practical_value: '- 业务侧若需对LLM做推理能力微调（如电商Agent复杂导购、下单逻辑推理），可直接引入SDP正则，无需额外安全训练数据即可保留原有安全对齐能力，避免微调后输出有害内容

  - 「提取目标功能的表征方向+分层施加正则」的思路可迁移到推荐多目标优化场景：比如要提升召回准确率同时不伤害多样性，可提取两个目标的表征方向，对冲突方向的参数更新加惩罚

  - 用CKA距离定位功能敏感层的方法，可用于大模型微调效率优化：仅对目标层做LoRA微调，减少训练开销同时避免无关能力退化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
对LLM做纯无害推理数据SFT（数学、代码、CoT轨迹等无任何有害内容的数据）时，会出现推理诱导的对齐偏移（RIM）：模型推理能力保留甚至提升，但安全对齐能力显著下降，此前研究仅将其归因于神经元级纠缠，没有可落地的训练时修复方案，会导致业务中推理增强的LLM出现不可控的安全风险。

### 方法关键点
1. 从隐状态表征空间提取两个线性方向：推理方向（区分正确/错误推理输出的隐状态均值差）、安全方向（区分拒绝/满足有害请求的隐状态均值差），验证两者在中深层呈负相关，优化推理会反向偏移安全表征
2. 用CKA距离比定位安全决策层：即微调后有害输入表征变化幅度远大于无害输入的层，发现该层内模型仍能识别有害输入，但不再执行拒绝动作
3. 提出Safety-Direction Penalty（SDP）：在推理SFT的交叉熵损失中，新增安全方向上的隐状态位移平方惩罚，先对初始定位的安全层施加惩罚，若出现未惩罚层的补偿偏移则迭代扩大惩罚范围

### 关键结果
在Qwen2.5-3B、7B上测试，基线为普通推理SFT：3B的HEx-PHI有害率从20.3%降到10.0%（与基座持平），SafetyBench准确率从57.9%回升到69.6%；7B的有害率从25.3%降到11.3%（低于基座），SafetyBench准确率回到79.4%，推理性能仅下降2~3.8个百分点，无任何推理侧开销。

**最值得记住的一句话**：纯无害推理数据微调也可能破坏LLM原有安全对齐，通过表征空间方向约束可在几乎不损失推理能力的前提下修复安全问题。
