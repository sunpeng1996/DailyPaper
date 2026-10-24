---
title: Would an LLM Match into a Residency? Uncertainty, Reasoning and Image Use of
  Open Language Models on the Spanish MIR Examination
title_zh: 开源大模型在西班牙MIR住院医师考试中的能力综合评估
authors:
- Miguel Fernandez-de-Retana
- Unai Zulaika
- Ruben Sanchez-Corcuera
- Aritz Bilbao-Jayo
- Aitor Almeida
affiliations:
- Faculty of Engineering, University of Deusto (Bilbao, Spain)
arxiv_id: '2610.31586'
url: https://arxiv.org/abs/2610.31586
pdf_url: https://arxiv.org/pdf/2610.31586
published: '2026-10-22'
collected: '2026-10-24'
category: Eval
direction: 大模型垂直领域能力评估
tags:
- LLM
- Uncertainty Quantification
- Medical QA
- Open-Weight Model
- Evaluation
one_liner: 评估8-27B开源大模型在医考中的准确率、不确定性校准、推理可靠性与图像利用能力
practical_value: '- 可复用「基于任务固有基线（如四选一25%正确率）判断是否启用低置信度结果拒答」的评估逻辑，优化搜索推荐低置信query/结果的兜底策略

  - 可参考「垂域微调后同步验证置信度区分度而非仅看准确率」的校验方法，避免电商垂域微调LLM后置信度校准失效

  - 多模态LLM落地时可采用「移除/替换输入图像对比准确率」的低成本测试方法，快速验证模型是否真的利用了输入视觉特征'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM医疗能力评估多聚焦闭源模型准确率，缺少对开源模型不确定性校准、推理可靠性、多模态利用能力的系统性评估，无法满足私有化部署医疗机构的决策需求。
### 方法关键点
选取4个8~27B参数开源模型，在西班牙MIR住院医师考试的8届共1552道真题上，按考试规则评估答题表现、置信度校准能力、推理合理性、图像利用效果，对比医疗微调前后的性能变化。
### 关键结果数字
- 3款较大模型答题排名处于考生前600~3000名，可申请41~43个专科方向
- 即使模型最低置信度答案正确率也高于25%随机猜测基线，弃答无收益
- 医疗微调降低过自信但损失准确率，未提升置信度对对错答案的区分度
- 13%~38%正确答案存在不合理推理逻辑，且置信度无法识别该问题
- 移除/替换题干图像后模型准确率无变化，证明未有效利用输入视觉信息
