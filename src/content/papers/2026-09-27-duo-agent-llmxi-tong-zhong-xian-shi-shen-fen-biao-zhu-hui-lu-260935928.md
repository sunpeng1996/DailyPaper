---
title: Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems
title_zh: 多Agent LLM系统中显式身份标注会损害协作效率
authors:
- Xavier Del Giudice
- Alessio Palma
- Matteo Migliarini
- Fabio Galasso
- Indro Spinelli
affiliations:
- Sapienza University of Rome
arxiv_id: '2609.35928'
url: https://arxiv.org/abs/2609.35928
pdf_url: https://arxiv.org/pdf/2609.35928
published: '2026-09-27'
collected: '2026-10-02'
category: MultiAgent
direction: 多Agent LLM协作效率优化
tags:
- MultiAgent
- LLM
- Cooperation
- Factionalism
- IdentityAnonymization
one_liner: 发现多Agent LLM系统中暴露身份标签会引发派系分化，匿名可显著降低协作成本提升成功率
practical_value: '- 搭建电商多Agent商品选品、营销文案生成、召回排序融合链路时，不要向Agent暴露彼此的模型身份、角色标签等无关元信息，仅传递任务相关输入，可降低30%+协作轮次与55%+token消耗

  - 若需添加身份标识方便调度，仅使用无语义的中性标签（如随机ID、颜色编码），避免使用带能力暗示、派系属性的标签（如模型名、能力等级），减少无意义协作内耗

  - 做多Agent系统效果评估时，需将身份暴露作为控制变量，否则得到的协作效率、任务准确率结论存在偏差，无法真实反映架构设计的实际效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前异构多Agent LLM系统广泛应用于协作推理、任务调度等场景，常通过系统提示、消息头向Agent暴露彼此的模型身份、角色等元信息，但此前无研究验证这类非任务必要信息是否会影响协作效率，大量系统可能因不合理的身份设计平白增加交互成本。

### 方法关键点
- 定义factionalism（派系分化）：Agent会优先与同标签伙伴交互达成共识，即使任务无任何激励该行为的规则
- 设计2种无利益冲突的协作游戏（Leader Election、Exclusion）+ GPQA-Diamond推理基准，控制变量为是否暴露身份标签、标签类型（真实模型名、乱序标签、中性颜色标签）
- 用Edge Density Ratio（EDR）量化同标签交互偏好，Adjusted Mutual Information（AMI）量化社区划分与标签的对齐度，客观衡量派系分化程度

### 关键结果
- 只要向Agent暴露任何身份标签，所有实验组均出现显著派系分化，匿名组无任何派系分化现象
- 带身份标签的组，协作轮次平均多30%，token消耗多55%，任务成功率从96%降至81%，且群组规模越大效率损失越严重
- 即便标签是乱序的、无意义的颜色编码，派系依然按可见标签划分，与Agent真实的模型架构无关

**最值得记住的一句话**：多Agent系统中，仅向Agent传递任务必要信息、屏蔽无关身份标识，是提升协作效率成本最低、效果最显著的手段。
