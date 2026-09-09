---
title: Can Agents Win the Video Browser Showdown?
title_zh: 自主智能体能否在视频浏览器挑战赛（VBS）中超越人类专家？
authors:
- Bastian Jäckl
- Zuzana Vopálková
- Daniel A. Keim
- Jakub Lokoč
affiliations:
- University of Konstanz
- Charles University
arxiv_id: '2609.07311'
url: https://arxiv.org/abs/2609.07311
pdf_url: https://arxiv.org/pdf/2609.07311
published: '2026-09-07'
collected: '2026-09-09'
category: Agent
direction: Agent 自主多模态检索性能优化
tags:
- Video Retrieval
- Multi-Agent
- VLM
- Interactive Search
- VBS
one_liner: 提出自主多Agent视频检索框架，在VBS历史任务上性能接近人类专家水平
practical_value: '- 多Agent分工+共享状态的架构可复用在电商多模态商品检索、图片找同款等场景，实现全链路自主检索，降低用户操作成本

  - 可借鉴「意图明确后Agent自主调用检索工具、迭代查询、评估候选、超时兜底提交」的闭环逻辑，优化现有搜索推荐的交互流程

  - 候选验证环节加二级falsification校验Agent的trick可直接落地，能过滤33.1%的错误匹配，仅误拒4.9%的正确结果，适合广告素材审核、商品匹配等场景

  - Agent动作选择的反馈策略可参考：无相关结果时优先重写query，有部分相关结果时切换到单视频/局部检索，提升长尾召回效率'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
交互式视频检索长期依赖人类专家操作检索工具，认知成本高、效率不稳定；现有Agent视频检索方案大多停留在单模态查询生成或单任务场景，未系统验证自主Agent能否替代人类完成全流程多类型检索任务，也未与专家水平做标准化对比。

### 方法关键点
- 多Agent分工架构：Planner Agent统筹动作选择，Browser Agent自动评估候选relevance，Inspector Agent做定向信息查询，VQA Agent处理视频问答任务，Fallback Estimator负责超时兜底提交
- 全局共享搜索状态：存储任务编码、执行历史、候选评估结果、提交反馈等全链路信息，支撑多Agent协同和迭代决策
- 复用成熟检索后端：对接VBS冠军PraK系统的语义搜索、时序搜索、相关性反馈、单视频检索等能力，Agent仅做操作决策，无需重复开发检索能力
- 任务编码适配：视觉类任务转成文本描述输入，对齐VBS规则中不能直接用输入素材做相似检索的要求

### 关键实验
在2024-2026年共81个VBS历史任务上测试，与每年Top3的专家系统对比：
1. 文本已知项搜索：Agent完成率81.8%（9/11），8/9个共同完成的任务中Agent速度超过最快专家
2. Ad-hoc视频搜索：8/13个任务中Agent性能追平或超过最优专家，单轮5分钟可审核300+候选
3. 视频问答：Agent完成率68.7%-75%（11-12/16），接近专家的75%-87.5%（12-14/16），7-8个任务速度超过所有专家
4. 增加二级校验Agent可过滤33.1%的错误提交，仅误拒4.9%的正确结果

### 核心结论
在意图明确的场景下，自主Agent完全可以替代人类完成交互式检索的全流程操作，性能接近专家水平，未来人机分工可转向用户指定意图、Agent执行检索、人类做最终校验的模式
