---
title: 'LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds'
title_zh: LiveGeo：持续演进世界中地理智能体的决策能力评测基准
authors:
- Pengcheng Zhou
- Xuanyu Liu
- Yanchen Yin
- Tianjie Ju
- Bobo Li
- Shengqiong Wu
- Hao Fei
- Mong-Li Lee
- Wynne Hsu
affiliations:
- National University of Singapore
- Zhejiang University
- Beijing University of Posts and Telecommunications
- University of Oxford
arxiv_id: '2611.17267'
url: https://arxiv.org/abs/2611.17267
pdf_url: https://arxiv.org/pdf/2611.17267
published: '2026-11-12'
collected: '2026-11-13'
category: Agent
direction: Agent 动态时空决策能力评测
tags:
- LLM Agent
- Agent Evaluation
- Dynamic Environment
- Spatio-Temporal Reasoning
- Benchmark
one_liner: 构建可交互动态地理环境GeoWorld与配套基准LiveGeo，评测Agent在动态时空场景的决策可靠性
practical_value: '- 本地生活/出行/到店推荐类Agent可复用GeoWorld的状态管理架构：将静态地理结构（路网、POI属性）与动态状态（交通、营业状态、活动）解耦，用统一时间轴管理多维度动态变更，解决多工具返回状态不一致问题

  - 动态场景Agent决策模块可新增核心参数二次校验逻辑：论文验证后期查询占比与动态决策成功率正相关（r=0.6~0.8），决策输出前强制校验时效、营业状态等核心依赖，可大幅降低信息过期导致的错误

  - 动态Agent评测可复用LiveGeo的静态-动态配对任务设计：控制初始条件一致仅引入可控动态事件，可精准剥离环境动态性对Agent能力的影响，避免评测结果被初始任务复杂度干扰

  - 本地服务类实时推荐系统可优先解决变更感知问题：动态场景下79.4%的失败根因为变更监测失效，核心POI/约束的状态变更主动推送给决策模块，远优于让模块主动轮询的效果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有地理Agent评测均基于静态世界快照，或仅预设单种显式扰动，完全不符合真实世界中交通、天气、门店状态、城市活动持续独立演进的特点，无法评测Agent主动感知变更、校验决策依据有效性、动态调整规划的能力，也难以定位决策失败的根因。

### 方法关键点
1. 构建GeoWorld动态地理环境：基于上海、东京、新加坡等6个真实城市的POI、路网、区域数据，用统一时间轴管理交通、天气、门店状态、城市活动等多类独立演进的动态状态，对外提供地图、交通、天气、活动查询等统一工具接口，所有交互留痕可溯源。
2. 配套LiveGeo基准：覆盖原子任务（定位、POI查找、路径规划）、组合任务（多用户协调、长周期行程、安全感知、区域适配）共7类任务，合计1237个可验证实例，其中149对静态-动态匹配任务，控制初始条件一致仅引入动态事件。
3. 统一评测框架：所有模型基于ReAct Agent架构测试，工具调用协议、交互预算完全一致，从决策正确性、可执行性、证据支撑性、动态适配性四个维度评估结果。

### 关键结果
1. 静态场景下最优模型（Gemini 3.7 Flash）整体成功率仅26.2%，长周期行程类任务最优成功率仅8.7%，证据幻觉是最主要失败原因，占比37.3%。
2. 动态场景下所有模型平均成功率相比静态下降70.3%（仅任务相关动态）到79.3%（含无关干扰事件），最优模型动态成功率仅13.4%~14.1%。
3. 79.4%的动态场景失败根因为变更监测失效，Agent 80%以上查询集中在任务早期；即使Agent完整观测到所有变更，仍有超36%的情况会正确报告变更但给出错误决策。

**最值得记住的一句话**：静态决策能力强的Agent动态鲁棒性不一定强，可靠的动态时空决策不仅要会获取信息，还要会在正确的时间校验核心决策依据的有效性。
