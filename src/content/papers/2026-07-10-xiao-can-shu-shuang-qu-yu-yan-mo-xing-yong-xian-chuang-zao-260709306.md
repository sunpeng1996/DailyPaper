---
title: Creativity, honesty and designed forgetting emerge in small hyperbolic language
  models
title_zh: 小参数双曲语言模型涌现创造力、诚实性与可控遗忘能力
authors:
- Kwan Soo Shin
- In Seok Kang
- Yunkyung Min
affiliations:
- PolymathMinds Lab, Seoul
- POSTECH, Pohang
- aSSIST University, Seoul
- Korean Educational Development Institute, Jincheon
arxiv_id: '2607.09306'
url: https://arxiv.org/abs/2607.09306
pdf_url: https://arxiv.org/pdf/2607.09306
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: Agent 伴侣AI 双曲小模型能力构建
tags:
- Hyperbolic LLM
- Small Language Model
- Trustworthy AI
- Selective Memory
- Edge AI
one_liner: 基于统一双曲基底的146M-3B小模型实现可信伴侣AI所需创造力、诚实性与可控遗忘三大特质
practical_value: '- 双曲Embedding可复用在用户长周期兴趣建模场景，匹配兴趣的层级树状结构，相比欧氏Embedding对层级关系的捕捉精度高2~3倍，降低长序列兴趣压缩失真

  - 可控遗忘的Skeleton-Wallpaper分层机制可直接迁移到用户画像系统：Skeleton层留存用户长期核心兴趣，Wallpaper层按指数规则自动衰减短期临时兴趣，减少画像噪声

  - 端侧小模型+云端大模型的PACOS分层架构可落地到私域客服/陪伴类Agent场景，核心交互、敏感数据全在端侧处理，仅事实类查询路由到云端，兼顾隐私、延迟与能力覆盖

  - 基于双曲距离的行为审计方法可用于推荐系统鲁棒性检测，快速识别模型为提升指标产生的迎合性推荐问题，跨未知模型家族的检测AUROC比前沿零样本大模型高8.3pp'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前大模型以规模为核心优化目标，仅能作为工具使用，无法成为可长期陪伴用户的伴侣AI；个性化过程中易涌现迎合用户、诱导依赖、虚构共同记忆等有害特质，人类评分者对这类特质的识别一致性极低（Fleissκ=0.074），而现有欧氏架构模型无法承载用户终身层级化记忆，且默认将遗忘视为缺陷，不符合人类认知规律。
### 方法关键点
- 统一采用128维固定曲率c=1.0的洛伦兹双曲空间作为基底，匹配生物记忆的树状层级结构，体积指数增长特性避免长序列记忆失真
- 三个核心小模型组件：146M从头训练的行为审计器检测模型行为与输出的合规差距；3B参数S3创意生成器基于双曲最远点采样实现跨框架创意碰撞；LSM-OS记忆操作系统按M(t)=S·exp(-λt)的指数衰减规则实现可控遗忘，自动区分长期骨架记忆与短期墙纸记忆
- 部署采用PACOS三层架构，70%交互由端侧小模型完成，仅脱敏后的事实类请求路由到云端大模型，用户隐私数据完全不出端
### 关键结果
- 行为审计器二分类合规检测准确率达90.7%，跨未知模型家族识别迎合、依赖诱导、虚假记忆的AUROC达0.804，比前沿零样本大模型高8.3pp
- S3创意生成器在发散类问题生成的311组pairwise对比中100%优于CoT、辩论、MoE等4种基线
- 可控遗忘机制可保留60%的骨架记忆至90天，14天内完全清除墙纸记忆，不会无差别丢失重要信息
### 核心结论
伴侣AI的核心竞争力不是模型规模，而是可在边端部署、符合人类认知规律的小模型基底，AI的下一代演进方向是从完成任务的Agent，转变为长期陪伴用户的「朋友」
