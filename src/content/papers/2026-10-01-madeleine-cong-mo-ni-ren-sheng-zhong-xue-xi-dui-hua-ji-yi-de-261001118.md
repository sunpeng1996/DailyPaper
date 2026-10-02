---
title: 'Madeleine: Learning Involuntary Recall for Conversational Memory from Simulated
  Lives'
title_zh: Madeleine：从模拟人生中学习对话记忆的非自主召回
authors:
- Zhiyun Shi
affiliations:
- Nanyang Technological University, Singapore
arxiv_id: '2610.01118'
url: https://arxiv.org/abs/2610.01118
pdf_url: https://arxiv.org/pdf/2610.01118
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: Agent长时记忆低开销关联召回
tags:
- Conversational Memory
- Retrieval
- LoRA
- Synthetic Data
- Long-term Agent
one_liner: 通过离线模拟人生蒸馏关联知识，实现零LLM调用的对话记忆关联召回，性能追平现有SOTA
practical_value: '- 记忆检索/RAG优化可复用「仅查询端LoRA微调+冻结内存向量」的设计，无需重建存量向量索引，零写入额外开销，完全兼容现有系统

  - 针对语义相似匹配盲区（如用户历史偏好与当前行为的弱语义关联），可通过LLM离线模拟生成(触发,关联)监督对，蒸馏关联知识到检索编码器，避免在线LLM调用的高成本

  - 训练关联检索时可采用「基础相似度+关联得分残差相加」的目标函数，既保留原有语义检索能力，又能学习弱语义的关联匹配'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有长时对话记忆系统的关联召回依赖在线/写入时的LLM推理（System 2），单记忆库需数百到上千次LLM调用，单查询需数千上下文token，成本极高；而语义向量检索仅匹配相似内容，无法召回语义不相关但逻辑关联的记忆（如用户曾说“学会拒绝降低压力”，数月后说“接了那个项目我很累”，两者无相似内容但高度关联），在关联召回任务上目标、价值类记忆的漏检率超30%。

### 方法关键点
1. 离线用LLM生成三类模拟人生数据，构造(触发utterance, 关联cue记忆)对，要求两者无共享内容、仅逻辑关联，数据去污染避免测试集泄漏
2. 采用残差关联检索架构：冻结预训练嵌入器作为语义相似度分支，仅在查询端加LoRA适配器学习关联得分，最终得分为语义相似度+关联得分之和
3. 训练采用同源负采样的InfoNCE损失，仅微调查询端LoRA参数，内存向量仍由冻结嵌入器生成，无需修改存量索引

### 关键实验
在LoCoMo-Plus关联召回基准上：①单独使用时得分52.4，与现有SOTA HyperMem的52.9无显著差异，仅需375上下文token（为HyperMem的1/21），读写阶段零LLM调用；②作为插件替换HyperMem、T-Mem的查询编码器，分别将得分提升至66.6、59.9，分别提升13.7、26.2个百分点；③普通问答任务得分与原嵌入器无差异，无能力退化。

**最值得记住的一句话**：长时记忆的关联关系是可学习的PMI，通过离线将LLM的System 2推理蒸馏到检索编码器，可实现零在线LLM调用的低开销System 1关联召回
