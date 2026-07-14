---
title: 'PaperRouter-Agent: A Content-Grounded LLM Agent for Personalized Hierarchical
  Paper Routing'
title_zh: PaperRouter-Agent：面向个性化分层论文路由的内容锚定LLM Agent
authors:
- Keshen Zhou
- Lintao Wang
- Suqin Yuan
- Zhuqiang Lu
- Yu Luo
- Zhiyong Wang
affiliations:
- University of Sydney
arxiv_id: '2607.11564'
url: https://arxiv.org/abs/2607.11564
pdf_url: https://arxiv.org/pdf/2607.11564
published: '2026-07-13'
collected: '2026-07-14'
category: Agent
direction: LLM Agent · 个性化分层分类
tags:
- LLM Agent
- Personalized Classification
- Zero-Shot
- Hierarchical Classification
- RAG
one_liner: 无需训练的LLM Agent，锚定文件夹已有内容实现个性化分层论文路由，大幅提升分类召回
practical_value: '- 分层分类场景可复用四阶段架构：Planner做层级候选截断（类似推荐层级召回）、Retriever做分类规则前置（如电商属性/渠道类类目直接匹配元数据，跳过LLM推理），大幅降低推理成本

  - 个性化标签/类目分类场景，不要仅依赖类目/标签名称，可结合类目下已有样本做内容锚定验证，解决短命名、别名、用户自定义标签的歧义问题，适配电商用户自定义收藏夹、商家自定义商品分组的自动打标需求

  - 用户反馈无需做模型微调，可存入记忆库做相似样本的推理前注入，实现冷启动下的无训练个性化迭代，适合C端个性化工具类业务

  - 小样本/零样本分类场景，内容锚定验证+同类候选交叉对比的策略，可直接替代单轮Zero-Shot分类，LaMP-2基准上提升7%准确率，接近带检索的RAG方案且无需额外检索组件'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有分层文本分类依赖固定共享的专家分类体系，仅通过类目名称做匹配，无法适配用户自定义、动态演化的私有分类体系（如个人文献文件夹、用户自定义收藏夹、商家自定义商品分组等），这类私有分类的类目命名存在简写、多维度混合（主题/时间/状态/渠道）等问题，仅靠名称匹配误差极大。

### 方法关键点
- 四阶段无训练Agent架构：Planner做层级自上而下的候选截断，保留高置信分支避免错误剪枝；Retriever做类目类型识别，元数据类类目（年份/会议/渠道）直接匹配待分类对象元数据，跳过内容推理降本，主题类类目采样已有成员做验证；Inspector对待分类对象和类目成员做内容匹配，输出Fit/No-Fit/Abstain三类结果，再对多个Fit候选做交叉对比排序；Reflector存储用户的接受/拒绝反馈，相似样本推理时注入相关历史反馈做参考
- 全程无需用户侧训练，适配动态变化的私有分类体系

### 关键实验
1. 真实用户Zotero图书馆测试，对比单轮Zero-Shot baseline，整体Recall@1从0.39提升到0.61，Recall@3从0.57提升到0.83，其中元数据类类目（年份/会议）Recall@1从0.09提升到0.50；2. 公开LaMP-2个性化电影标签基准，准确率从44.5%提升到51.5%，macro-F1提升9个点，效果匹敌带独立检索模块的RAG方案，且无需额外检索组件。

### 核心结论
面向用户自定义的私有分类场景，锚定类目下的已有内容而非仅依赖类目名称，是零样本下提升分类效果的核心思路。
