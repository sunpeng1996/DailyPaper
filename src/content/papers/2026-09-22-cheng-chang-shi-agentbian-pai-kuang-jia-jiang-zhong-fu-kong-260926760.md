---
title: 'Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable
  Specialist Agents'
title_zh: 成长式Agent编排框架：将重复控制逻辑转化为可复用代码降低推理成本
authors:
- Laizhen Li
- Jiarui Li
- Juanjuan Zhao
- Kejiang Ye
- Ye Li
- Cheng-zhong Xu
- Xitong Gao
affiliations:
- Shenzhen Institutes of Advanced Technology, CAS
- University of Chinese Academy of Sciences
- Shenzhen University of Advanced Technology
- University of Macau
arxiv_id: '2609.26760'
url: https://arxiv.org/abs/2609.26760
pdf_url: https://arxiv.org/pdf/2609.26760
published: '2026-09-22'
collected: '2026-09-23'
category: Agent
direction: Agent 编排框架优化 · 低成本部署
tags:
- LLM Agent
- Harness Optimization
- Cost Efficiency
- Small LLM Deployment
- Failure Guided Learning
one_liner: 提出失败引导的成长式Agent编排范式，将重复控制沉淀为代码，大幅降低推理成本并提升小模型Agent效果
practical_value: '- 对于电商导购/客服类垂直Agent，可复用该框架把重复的查询解析、结果过滤、流程跳转逻辑沉淀为代码，可减少70%+的LLM调用，降低推理成本同时提升稳定性

  - 小模型部署场景可以参考该思路，把需要复杂推理的语义判断留给LLM，把确定的控制逻辑固化到编排层，能大幅拉平小模型和大模型的任务成功率差距

  - 迭代Agent编排逻辑时可采用失败窗口+held-out门控回滚机制：每次只修改失败路径关联的局部函数，上线前校验旧任务成功率不下降，避免能力退化'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent的控制逻辑要么提前硬编码要么每次靠LLM在上下文里生成，重复执行同类任务时频繁调用LLM导致成本高、小模型效果差，上下文膨胀还会降低推理准确性，针对同一任务域的Agent需要更高效的控制逻辑复用方式。

### 方法关键点
- 初始从无预设控制逻辑的空白脚手架开始，仅暴露固定的LLM和工具接口
- 每次执行失败后通过函数级执行轨迹定位故障代码范围，离线优化器仅修改关联的局部函数，编辑范围可控
- 维护固定大小的失败任务窗口，联合修复多个失败任务以生成可复用的控制逻辑，而非单任务补丁
- 新增held-out门控校验：修改后的编排代码需在验证集上成功率不下降才会被接受，否则回滚，避免能力退化

### 关键实验
在BrowseComp-Plus和WebArena-Verified两个Agent基准上，对比Tool-Calling、IRCoT、WebDreamer等基线，用4B、20B、120B三个尺寸的模型测试：6组测试场景中5组取得最高成功率，剩下1组仅比最优低0.7pp；相对Tool-Calling基线，LLM调用量降低76.0%~91.8%，在线推理成本降低74.4%~98.6%；WebArena-Verified基准上，4B小模型采用该框架成功率保持44.7%~45.3%，而Tool-Calling基线仅6.7%。

**最值得记住的一句话：同类任务域的Agent不需要每次让LLM重复生成控制逻辑，把可复用的控制沉淀到代码层、把LLM仅用于任务专属的语义推理，是平衡效果和成本的核心路径**
