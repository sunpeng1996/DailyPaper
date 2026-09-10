---
title: The Answer Path and the Grounding Instruction in LLM Question Answering over
  Knowledge Graphs
title_zh: 面向知识图谱问答的LLM回答路径与接地指令效果评估
authors:
- Arquimedes Canedo
affiliations:
- Siemens Digital Industries Software
arxiv_id: '2609.10237'
url: https://arxiv.org/abs/2609.10237
pdf_url: https://arxiv.org/pdf/2609.10237
published: '2026-09-09'
collected: '2026-09-10'
category: RAG
direction: GraphRAG 组件效果量化评估
tags:
- GraphRAG
- Knowledge Graph
- Retrieval
- Prompt Engineering
- LLM Evaluation
one_liner: 通过3万余组受控实验明确GraphRAG核心影响因子，否定多个常用优化点的实际价值
practical_value: '- 搭建电商商品/用户行为知识图谱RAG时，优先将预算倾斜到回答路径的召回率保障上，测试范围内检索精度优化、三元组序列化格式选择、排序规则调整、子图大小控制对最终答案准确率几乎无影响，ROI极低

  - 做LLM/RAG效果评测时必须严格对齐prompt：有上下文实验组和无上下文基线必须使用完全相同的接地指令，否则会得到「上下文损害多跳推理效果」的虚假结论

  - 结构化知识RAG的三元组序列化无需纠结格式，只要保证谓词为人类可读名称即可，多跳推理场景下不同格式的效果差异可忽略

  - 不要盲目给多跳推理RAG加思维链、分步推理类prompt，本文实验中这类prompt会使2-3跳推理F1下降0.02~0.043，反而损伤效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前GraphRAG管线的四大设计选择（召回三元组筛选、序列化格式、排序规则、系统提示词）缺乏量化的效果对比，从业者普遍不清楚优化投入的优先级，大量常用优化策略的实际价值没有经过严格受控实验验证，甚至存在错误评估导致的虚假结论。
### 方法关键点
- 采用正交控制变量设计，固定其他变量仅修改单一维度，覆盖6款主流商用LLM（GPT-5、Claude、Gemini全系列共2个能力层级）、2个知识图谱问答基准数据集（LC-QuAD 2.0、QALD），总计16组实验、30841次推理
- 测试变量包含：召回精度、接地指令（严格/宽松）、7种三元组序列化格式、5种三元组排序规则、0~200三元组的子图大小、1~4跳推理深度
- 双轴评估：token级F1衡量答案准确率，证据忠实度衡量引用知识的可靠性
### 关键结果
- 固定子图大小为50三元组，仅替换非回答路径的无关三元组，答案F1仅波动+0.003，无统计显著性；删除回答路径则严格prompt下F1暴跌至0.005，宽松prompt下跌至0.231
- 无上下文时，严格接地指令会将F1从0.299压至0.035，下降8.6倍；若无上下文基线用宽松prompt、上下文组用严格prompt，会得到「3~4跳推理时上下文有害」的虚假结论
- 三元组序列化格式、排序、子图大小在多跳推理场景下无显著效果影响，仅1跳场景下带可读谓词名的格式效果更优
- 思维链prompt使2~3跳推理F1下降0.02~0.043，反而损伤效果

**最值得记住的一句话：GraphRAG优化只需抓回答路径召回和接地指令设计两个核心点，其他维度优化ROI极低，甚至可能带来负收益**
