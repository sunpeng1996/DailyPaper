---
title: 'Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use
  Co-Evolve'
title_zh: 将知识图谱视为文件：实现工具创建与使用协同演化的Agent框架
authors:
- Yuyang Bai
- Yu Wang
- Yu Zhang
affiliations:
- Texas A&M University
- University of Oregon
arxiv_id: '2610.18616'
url: https://arxiv.org/abs/2610.18616
pdf_url: https://arxiv.org/pdf/2610.18616
published: '2026-10-13'
collected: '2026-10-14'
category: Agent
direction: Agent 知识图谱检索交互优化
tags:
- LLM-Agent
- Knowledge-Graph
- Tool-Use
- Graph-Retrieval
- Training-Free
one_liner: 提出无预定义图接口的DKGI框架，让LLM Agent直接操作图谱文件实现工具创用协同，性能超现有SOTA
practical_value: '- 电商商品、用户、行为知识图谱可导出为标准化文本文件格式，无需维护复杂图API，大幅降低Agent检索图谱的对接成本

  - 可复用多轮代码迭代交互范式：让Agent根据执行反馈动态修改图谱遍历代码，相比单轮预定义工具调用，复杂多跳检索Hit@1提升6.9个点

  - 大输出采用头尾截断+完整结果存本地文件的处理方案，既节约LLM上下文窗口，又避免信息丢失，适合大规模图谱检索场景

  - 训练免微调架构可直接复用，对接业务私域图谱时仅需修改格式说明文档，无需额外数据标注训练'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM Agent访问知识图谱依赖预定义API、检索器等接口，接口的返回限制（比如邻居查询最多返回20条）会导致关键证据丢失，即使通过代码组合工具调用也无法突破接口约束，复杂多跳检索准确率长期受限。

### 方法关键点
- 提出DKGI（Direct Knowledge Graph Interaction）框架，将完整知识图谱导出为标准化文本文件：节点按ID分块存储为JSONL，每个关系对应独立TSV边表，附带Schema和格式说明
- Agent采用ReAct交互范式，可自由混合Shell搜索、文件查看和Python代码执行，自主编写/迭代图谱访问工具，无需预定义任何图操作接口
- 大执行结果采用头尾截断+完整内容存本地文件的处理方式，后续代码可直接读取文件复用中间结果，避免上下文溢出
- 工具创建与使用协同演化：执行反馈指导代码修订，更新后的工具又指导后续证据收集，全程无需模型训练

### 关键实验
在STaRK基准的Amazon、MAG、Prime三个领域数据集上测试，训练免费的DKGI（搭配GPT-6-Astra）比最强已发布基线GRASP的Hit@1分别高8.2、9.0、6.7个点；消融实验显示，相比仅用Shell访问或单轮Python执行，多轮代码迭代的方案整体Hit@1提升6.9个点，比预定义图工具方案高2.4个点。

最值得记住的一句话：对于复杂多跳知识检索场景，放开Agent的底层数据访问权限、让其自主迭代工具，比优化预定义工具集的收益更高。
