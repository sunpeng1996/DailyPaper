---
title: 'AURA: Agentic Diagnosis and Refinement for Production Recommender Systems
  at Scale'
title_zh: 面向大规模生产推荐系统的Agent化诊断与优化框架AURA
authors:
- SungGeun Kim
- Abhinav Narain
- Daniel Nemirovsky
affiliations:
- The Walt Disney Company
- Intuit
arxiv_id: '2609.16625'
url: https://arxiv.org/abs/2609.16625
pdf_url: https://arxiv.org/pdf/2609.16625
published: '2026-09-15'
collected: '2026-09-16'
category: Agent
direction: Agent 推荐系统故障自动化诊断优化
tags:
- LLM Agent
- Recommender System
- Failure Diagnosis
- Production System
- Code Generation
one_liner: 构建多阶段Agent流水线，自动挖掘推荐系统细粒度故障并输出代码级可落地优化方案
practical_value: '- 故障诊断环节可复用「分层Agent聚合+先开放枚举后锁定分类taxonomy」的设计：先做小样本开放发现故障类别，再切换成固定分类大幅降低标注噪声，适配电商搜推的品类偏好、价格敏感、合规等多维度故障排查

  - 成本优化可复用「多模型路由策略」：高并发的分类、聚合任务用轻量小模型，高复杂度的根因分析、代码生成用前沿大模型，文中AURA自身分析成本仅占总投入的1%-8%，可直接落地到现有LLM评估流程

  - 生产级Agent系统的安全设计可直接复用：全链路读权限控制、代码修改仅在沙箱运行、所有输出带原始证据供人工校验、边界层加可编程校验（ID合法性、JSON格式、代码路径存在性），规避Agent幻觉导致的生产风险

  - 跨场景迁移可采用「核心代码+配置层分离」架构：领域相关的Session定义、故障分类、阈值规则全放在配置层，不需要修改核心逻辑即可从流媒体推荐迁移到电商搜推场景'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统依赖AUC、NDCG等聚合指标，无法暴露细分人群/场景的细粒度故障（比如电商过度推送高毛利商品给价格敏感用户、儿童账号收到不适内容），人工排查依赖domain经验效率极低，A/B测试成本高、诊断能力弱，亟需可规模化的自动化诊断优化方案。

### 方法关键点
- 四阶段流水线：1）会话选择：混合规则、采样、Agent筛选定位可疑会话cohort；2）诊断层：分层Agent聚合处理十万级以上会话，先分类再合并低信号类别，输出带严重度、证据、根因假设的故障分类；3）方案生成：接入推荐系统代码、特征、训练pipeline上下文，生成针对性技术提案；4）代码实现：生成pull request，加交叉校验规避幻觉。
- 成本控制：多模型路由，高吞吐任务用轻量模型，复杂分析/代码生成用前沿大模型；全链路加可编程校验，过滤幻觉输出（伪造ID、非法路径等）。
- 跨域适配：核心代码与配置层分离，领域规则全通过配置注入，可跨场景迁移。

### 关键实验
在迪士尼两个流媒体生产平台验证，会话规模分别为9.68万、10.16万，上游LLM judge准确率分别为96%、87.6%；迭代优化后全链路rubric评分从15/25升至23/25（平台A）、17/25升至24/25（平台B）；单轮端到端成本分别为349美元、253美元，AURA自身分析成本仅占8%、1%；产出的优化提案离线验证无指标负向，避免无效A/B测试投入。

最值得记住的一句话：工程师对Agent输出的信任来自可核验的结构化证据，而非大模型生成的叙事性解释。
