---
title: 'Wayfinder: Adaptive Resource Routing from Agent Citations'
title_zh: Wayfinder：基于智能体引用的自适应资源路由框架
authors:
- Miguel Romero
- George Karypis
affiliations:
- University of Minnesota
arxiv_id: '2611.16053'
url: https://arxiv.org/abs/2611.16053
pdf_url: https://arxiv.org/pdf/2611.16053
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: Agent 跨资源自适应路由优化
tags:
- Agent
- Resource Routing
- Reinforcement Learning
- LoRA
- Federated Search
one_liner: 基于Agent引用反馈实现无标注自适应资源路由，降低跨资源检索重复探索成本
practical_value: '- 电商/企业客服Agent跨多源知识库（商品库、工单、FAQ、评论）路由场景，可复用citation-gated反馈机制：仅将Agent回答时实际引用的文档更新到对应资源画像，避免无效检索结果、幻觉引用污染记忆，提升路由准确率

  - 跨环境零样本部署的训练trick：训练时匿名化资源ID、会话级随机置换资源标识，防止模型过拟合训练环境的资源名-主题关联，大幅提升新环境泛化性，该方法可直接迁移到所有跨环境工具选择任务

  - 资源受限生产场景的架构选择：用LoRA微调小参数路由策略，搭配LRU淘汰的bounded resource sketch存储，存储、计算成本低，无需全量索引资源内容，适配黑盒API访问的异构资源场景

  - 路由方案选型参考：若业务场景下多个资源语义重叠度高（如不同类目商品的评价、客服工单内容交叉），优先选择自适应反馈路由；若资源区分度高（如视频、商品、资讯分库），静态描述的工具检索就足够用'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM Agent执行用户任务时需跨聊天记录、工单、知识库、邮件等异构资源检索上下文，现有基于静态资源描述的路由方法无法区分语义重叠的资源，也无法从历史交互中迭代优化，每次新会话都要重复探索，效率极低；同时现有路由方法依赖目标环境的标注数据训练，无法零样本部署到新的企业/用户环境。
### 方法关键点
- 引入citation-gated反馈机制：仅将下游Agent回答时实际引用、且确实来自检索结果的文档纳入更新，过滤无效检索结果、幻觉引用，保证信号质量
- 每个资源维护LRU淘汰的bounded resource sketch，存储历史引用的文档、对应查询、时间戳，存储成本可控，无需全量索引资源内容
- 用GRPO强化学习训练LoRA微调的路由策略，训练时做会话级资源ID匿名+随机置换，防止模型过拟合训练环境的资源-主题关联，提升跨环境泛化性
- 路由结果为建议性而非强制性，Agent仍可搜索推荐外的资源，保证反馈信号不会因路由错误中断
### 关键实验
在三类测试集上对比7种基线：1. 语义重叠的同语料拆分数据集NFCorpus、FEVER上，Wayfinder路由F1达47.67、64.72，较最强基线分别高14.64、33.71，同时减少Agent搜索调用量61.2%、73.7%；2. 资源区分度高的跨语料Tech Startup数据集上，静态工具检索ToolRetriever最优（F1 98.86），Wayfinder以86.60排第二，优于需要目标环境标注的Learn2Rank。
### 核心结论
资源语义重叠度越高，基于交互反馈的自适应路由相对静态描述路由的优势越大，反之静态路由即可满足需求
