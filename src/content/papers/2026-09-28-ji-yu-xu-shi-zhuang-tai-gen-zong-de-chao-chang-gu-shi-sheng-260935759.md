---
title: Scaling Long-Form Story Generation via Narrative State Tracking
title_zh: 基于叙事状态跟踪的超长故事生成规模扩展方法
authors:
- Zhennan Wan
- Jianfei Chen
affiliations:
- Tsinghua University
arxiv_id: '2609.35759'
url: https://arxiv.org/abs/2609.35759
pdf_url: https://arxiv.org/pdf/2609.35759
published: '2026-09-28'
collected: '2026-09-29'
category: Agent
direction: Agent长文本生成 · 叙事状态跟踪
tags:
- LLM Agent
- Long-Form Generation
- Narrative State Tracking
- Consistency Evaluation
- Training-Free
one_liner: 提出免训练Agent框架NSTAGENT，通过跟踪结构化叙事状态实现10万词级高一致性长故事生成
practical_value: '- 电商长文案、系列种草文、连载内容生成场景可复用结构化叙事状态跟踪设计，替代传统滚动摘要方案，解决上万字长文本前后人设、情节、商品参数不一致问题，成本随文本长度线性增长

  - 长文本自动评估可借鉴固定窗口错误密度计算方法，针对长文案、多轮推荐话术的一致性评测，限制裁判判断窗口长度，避免长上下文下LLM裁判召回率下降导致的评估结果失真

  - 内容生成Agent链路可复用本工作的免训练工具调用架构，搭配历史文本检索、错误修正工具，无需微调LLM即可提升长内容生成质量，大幅降低业务落地成本

  - 长序列生成的长度控制可参考章节拆分解耦思路，每章单独做长度校验，避免单调用生成长文本的长度波动问题，提升生成可控性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM长故事生成最多支持万词级别，更长文本下叙事一致性随长度增长超线性下降；微调长文本生成模型成本高、高质量超长训练数据稀缺，分层规划的静态大纲无法适配写作过程中新增的细节，自由文本记忆方案容易丢失关键伏笔、人设等信息，且缺乏跨长度的可比一致性评估标准。
### 方法关键点
- 免训练Agent框架NSTAGENT分两阶段生成：先生成固定章节级大纲，再逐章写作并动态更新结构化叙事状态
- 叙事状态包含三类结构化信息：角色状态（位置、目标、关系等）、已发生事件、未落地的叙事承诺（伏笔、悬念等），每章生成后增量更新而非重写全量记忆
- 配套4类工具：read（读取历史章节）、search（BM25检索历史片段）、write（提交章节并校验长度）、correct（修正历史章节错误）
- 优化长文本一致性评估方案，采用固定10K词终端窗口统计错误密度（CED），避免长文本下LLM裁判召回率下降导致的评估不可比
### 关键实验
基于ConStory-Bench的100条英文prompt，对比Direct、DOME、RollSum等基线，覆盖10K~100K词长度，双骨干验证效果稳定：100K词场景下，DeepSeek-V4-Flash的Instance CED比RollSum低38.8%（7.24 vs 11.82），写作质量提升2.7%（9.20 vs 8.96）；生成成本随长度线性增长，R²达0.997，一致性和写作质量均不随长度明显下降。
### 核心结论
长序列生成的一致性瓶颈本质是记忆的结构化程度不足，用结构化可更新的状态替代自由文本摘要，可在免训练前提下大幅提升超长文本生成的稳定性。
