---
title: 'Agent Retrieval Bench: Evaluating Repository Context Retrieval for Coding
  Agents'
title_zh: Agent Retrieval Bench：面向编码Agent的代码仓库上下文检索评测集
authors:
- Bowen Qin
- Yi Xie
affiliations:
- National University of Singapore
- Peking University
arxiv_id: '2607.24882'
url: https://arxiv.org/abs/2607.24882
pdf_url: https://arxiv.org/pdf/2607.24882
published: '2026-07-26'
collected: '2026-07-30'
category: Agent
direction: Agent 代码上下文检索评测
tags:
- Agent
- Retrieval Benchmark
- Coding Agent
- Context Retrieval
- RAG
one_liner: 提出面向编码Agent上下文获取阶段的专用文件级代码检索基准，覆盖多类任务与无黄金样本评测
practical_value: '- 垂直场景RAG检索不要仅依赖语义相似度定义目标，需结合任务工作流相关性设计召回逻辑：比如电商客服场景用户咨询的召回目标可能是关联售后规则、商品参数，而非字面相似的其他咨询

  - 多召回通路融合可直接复用RRF策略：语义embedding、结构特征召回（如电商类目关联、商品从属关系）做秩融合，能显著提升整体召回效果，无需额外训练

  - 评估检索系统可引入BCY（Budgeted Context Yield）指标，衡量固定token/资源预算下有效上下文的获取效率，更贴近线上Agent的实际运行约束

  - 做选择性召回（拒答判断）时，不能仅靠top检索得分设阈值，要区分明显不匹配的反例和场景内确实无结果的情况，避免阈值校准偏差误杀正常召回请求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有编码Agent评测多聚焦最终补丁生成效果，忽略上游上下文获取阶段的性能，而上下文检索准确率直接影响Agent的工具调用成本、响应延迟与最终效果；传统代码搜索以query和文档的语义相似度为相关性标准，不符合编码Agent工作流中相关性由下一步任务需求决定的实际场景，缺少专用评测基准。

### 方法关键点
- 基准覆盖4类正向检索任务：code2test（从PR/代码变更召回关联测试用例）、comment2context（从代码评审评论召回所需额外上下文文件）、trace2code（从错误日志召回根因代码文件）、edit2ripple（从代码变更召回受影响的关联文件），新增2类无黄金样本集：自然无结果案例、错误仓库反例，合计427个样本，覆盖25个开源仓库
- 相关性定义为Agent完成下一步任务所需读取的文件，而非字面/语义相似；评测指标除常规Recall@k、MRR外，新增BCY@B衡量固定token预算下的有效上下文获取率，新增PES@k衡量检索对Agent探索成本的潜在节省空间
- 对比词法检索、BM25、RepoMap结构检索、多款开源代码embedding模型效果，同时验证静态检索与交互式Agent轨迹的互补性

### 关键结果
- 345个正向样本上，Qwen3-Embedding-4B取得最优加权MRR（0.2379），Qwen3-Embedding-8B取得最优Recall@20（0.7029），RepoMap结构检索取得最优BCY@8k（0.3788），不同任务最优模型差异显著
- 用RRF融合Qwen3-8B和RepoMap的结果，整体MRR从0.2296提升至0.2713，Recall@20从0.7070提升至0.7331，验证语义和结构检索的互补性
- 静态检索top20能覆盖80%以上交互式Agent晚命中（超过3步才找到黄金文件）案例的目标，优质初始检索种子可减少Agent40%以上的后续探索成本
- 现有基于top检索得分的阈值法无法有效处理自然无黄金样本的选择性召回需求，存在明显校准偏差

**最值得记住的一句话**：Agent场景的检索优化不能只看语义匹配指标，要结合任务工作流定义目标，融合语义和结构特征的召回策略能兼顾效果和效率
