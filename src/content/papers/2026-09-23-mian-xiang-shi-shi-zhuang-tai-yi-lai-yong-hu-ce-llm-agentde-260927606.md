---
title: 'State-Grounded Conditioning: Wrapping User-Facing LLM Agents Where Direction
  Depends on Live State'
title_zh: 面向实时状态依赖用户侧LLM Agent的状态感知条件化方案
authors:
- Qi Liu
- Xiaoyang Yuan
- Yubin Ruan
- Zhuomeng Zhang
- Wenjin Wang
- Di Wu
- Mingye Xu
- Xinyi Mou
- Xingxi Yin
- Ke Feng
affiliations:
- Tencent
arxiv_id: '2609.27606'
url: https://arxiv.org/abs/2609.27606
pdf_url: https://arxiv.org/pdf/2609.27606
published: '2026-09-23'
collected: '2026-09-24'
category: Agent
direction: LLM Agent 实时状态对齐优化
tags:
- LLM Agent
- State Alignment
- Direction Drift
- Low Latency
- Grounding
one_liner: 提出SGC三wrapper架构，解决实时用户Agent方向漂移问题，降延迟提准确率
practical_value: '- 电商实时导购/直播带货Agent可直接复用三wrapper分层设计：Perception层提前识别用户意图调用工具降低首token延迟，解决高并发下响应超时问题；Grounding层对齐用户实时购物车、商品库存、历史偏好等结构化状态，避免推荐已售罄/用户已购商品这类槽漂移错误；Interaction层记录会话历史做推荐冷却，避免重复推荐相同商品的疲劳漂移

  - 可复用方向漂移的评估思路：现有生成式推荐/Agent评估多关注任务完成率，可新增turn级/会话级状态对齐准确率指标，量化推荐方向与用户实时状态的匹配度，更早发现业务bad
  case

  - 工程上可借鉴结构化规则与LLM解耦的设计思路：把状态对齐的控制逻辑用确定性规则实现，LLM只负责自然语言生成，既降低大模型调用次数控本，又让规则迭代更灵活，无需反复微调大模型'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前生产环境的实时用户侧LLM Agent（如游戏陪练、电商导购、智能客服）普遍存在「方向漂移」问题：输出语法正确、表面完成任务，但推荐/回复方向与用户实时状态（游戏状态、商品库存、会话历史）完全不匹配。现有Agent编排框架只关注任务完成率，未解决动态状态对齐问题，且串行规划流程导致首token延迟过高，无法满足实时交互要求。

### 方法关键点
- 提出State-Grounded Conditioning（SGC）设计原则，将状态依赖的控制逻辑从大模型推理中剥离，用确定性规则实现，结果作为控制变量注入生成上下文
- 三个近似正交的wrapper分别对应三类状态切片：
  1. Perception Wrapper：单流4合1解码识别意图，子意图识别完成后立即提前调度工具，无需等待完整规划结果，解决延迟漂移
  2. Grounding Wrapper：独立提取请求槽位，与实时事实（如库存、用户资产）做diff分级，确定性判定可生成的候选内容，解决槽漂移和一致性漂移
  3. Interaction Wrapper：基于会话历史做推荐冷却，注入随机种子保证会话可复现，解决疲劳漂移

### 关键实验
在200会话（约1000轮交互）的游戏陪练Agent生产基准上测试，对比Prompting、PE-Agent两个基线：仅开启Perception Wrapper即可将首token latency从PE-Agent的6.1s降到1.5s；全量SGC将turn级状态对齐准确率从69.8%（PE-Agent）提升到96.7%，会话级对齐准确率从26.5%提升到83.5%，会话级对齐失败率相对下降78%。

### 最值得记住的一句话
实时用户Agent的核心矛盾不是任务能不能完成，而是完成任务的方向是否与用户当前动态状态对齐，规则化状态对齐层相比纯大模型端到端推理，在成本、延迟、可控性上都有显著优势。
