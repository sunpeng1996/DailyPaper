---
title: 'Same Behavior, Different Mechanism: What Finite Experiments Can Certify About
  Integrated Information'
title_zh: 相同行为不同机制：有限实验对整合信息的可验证边界研究
authors:
- Linqian Wu
- Diaoxuan He
affiliations:
- University of Waterloo
- Perimeter Institute for Theoretical Physics
- University of Debrecen
arxiv_id: '2611.08469'
url: https://arxiv.org/abs/2611.08469
pdf_url: https://arxiv.org/pdf/2611.08469
published: '2026-11-05'
collected: '2026-11-08'
category: Eval
direction: AI机制度量 · 有限实验验证方法
tags:
- Interpretability
- AI Auditing
- Causal Inference
- Integrated Information
- Finite Sample
one_liner: 明确了机制级度量整合信息φ在有限干预实验下的可测性计算边界
practical_value: '- 做黑盒推荐模型/Agent的机制审计时，可参考因果干预+下界验证的思路，避免仅靠输入输出匹配判定内部逻辑一致性

  - 有限样本下计算机制级度量时，优先输出单侧下界结论，可大幅降低样本不足带来的度量误差

  - 涉及分区选择的业务指标（如多模态融合权重、召回通路贡献）设计时，需提前评估边界跳变带来的鲁棒性问题'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
AI可解释性、模型审计、意识评估高度依赖机制级度量（描述系统计算逻辑而非输出结果），但这类度量仅能通过有限、有噪、局部的干预实验观测，其可识别性、鲁棒性缺乏明确边界。
### 方法关键点
以整合信息理论核心度量φ为测试对象，在4-5单元随机网络、奇偶校验网络等受控场景下，测试三类场景下的φ可测性：输入输出行为完全匹配、仅能观测部分单元、度量存在决策边界。
### 关键结果
1. 输入输出完全一致的循环/前馈网络φ分别为0.28/0 bits，仅需4-53次内部观测即可区分；
2. 单步部分观测存在0.30-1.02 bits的精度下限，无法通过增加样本量消除；
3. 99%的φ度量边界上，机制微小变化会导致φ跳变25%-100%，1%拟合极好的代理模型φ度量误差超20%；
4. 约1e7次受控干预可验证φ>1.004 bits，假阳性率可控为α。
