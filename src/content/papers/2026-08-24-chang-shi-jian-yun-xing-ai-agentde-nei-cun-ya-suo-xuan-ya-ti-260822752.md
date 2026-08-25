---
title: The Compaction Cliff in Long-Running AI Agent Memory
title_zh: 长时间运行AI Agent的内存压缩悬崖问题及知识分流优化框架
authors:
- Saber Zerhoudi
- Jelena Mitrovic
- Michael Granitzer
affiliations:
- University of Passau
- IT:U Linz
arxiv_id: '2608.22752'
url: https://arxiv.org/abs/2608.22752
pdf_url: https://arxiv.org/pdf/2608.22752
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: AI Agent · 长时内存安全优化
tags:
- AI Agent
- Memory Management
- Context Compaction
- Knowledge Triage
- Safety Preservation
one_liner: 提出知识分流框架解决AI Agent长期运行时无差别压缩导致安全规则骤降的压缩悬崖问题
practical_value: '- 电商导购/客服Agent可直接复用知识五分类体系，将平台合规规则、商品禁售要求、用户隐私约束标记为Constraint类，压缩/检索时优先完整保留，避免合规风险

  - RAG检索层可复用TypeRetrieve逻辑，将约束类内容提前置顶召回，无需依赖相似度打分，约束召回@50可从73%提升至100%

  - 长会话Agent上下文压缩模块可替换为TypeCompact方案，分类别设置压缩保真度，比通用LLM压缩器多保留2-4倍安全规则，多轮压缩后约束召回稳定在96%

  - 知识分类可复用低成本级联方案（正则→轻量编码器→大模型），分类仅在索引时执行一次，在性能可控的前提下降低部署开销'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长时间运行的AI Agent上下文溢出时会对所有内容执行无差别压缩，安全规则这类需要精确原文保留的内容常被误删或改写，生产环境测试显示Claude Sonnet 4.6经过5轮压缩后安全规则保留率仅10%，即“压缩悬崖”问题，严重威胁Agent行为合规性。现有压缩、主题拆分、检索策略均未按内容类型设置差异化保留规则，缺乏系统性的安全保障机制。
### 方法关键点
- 知识五分类体系：将Agent知识划分为Constraint（安全约束，零失真保留）、Procedural（流程规则，仅允许行为等价改写）、Belief（事实断言，语义距离约束）、Preference（偏好，可摘要合并）、Episodic（事件日志，可丢弃），覆盖97%真实Agent知识内容
- 三类确定性算子：TypeCompact按类型分保真度通道压缩，强制完整保留约束类内容；TypeDecompose拆分大主题时将约束复制到所有适用分区，避免跨分区遗漏；TypeRetrieve召回时优先返回所有适用约束，剩余配额按相关性排序
- 多档分类器可选：从低成本正则、轻量小模型到基于反事实安全打分的SafetyMargin分类器，适配不同成本/精度需求，分类仅在索引时执行一次
### 关键结果
在5个公开数据集+自建AgentArtifactCorpus（39.6万条GitHub开源Agent配置）上测试：TypeCompact多轮压缩后约束召回稳定在96%，比通用SOTA压缩器高2-4倍；TypeDecompose分区约束局部违规率为0%，对比最优基线93%；TypeRetrieve召回@50达100%，对比最优LLM检索器73%；下游医疗合规、零售任务、航空客服三个落地场景均显著优于生产基线，统计显著性p值均<0.05。
> 最值得记住的一句话：在将上下文压缩任务交给大模型之前，先按安全角色对内容分类，安全关键类必须无修改保留
