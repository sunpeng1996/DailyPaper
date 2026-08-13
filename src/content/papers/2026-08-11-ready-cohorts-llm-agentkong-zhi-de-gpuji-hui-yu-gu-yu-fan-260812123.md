---
title: 'Ready Cohorts: Bounding GPU Opportunity and Avoiding Host Round Trips in LLM-Agent
  Control'
title_zh: Ready Cohorts：LLM Agent控制的GPU机会预估与Host往返优化
authors:
- Josef Liyanjun Chen
affiliations:
- Independent Researcher
arxiv_id: '2608.12123'
url: https://arxiv.org/abs/2608.12123
pdf_url: https://arxiv.org/pdf/2608.12123
published: '2026-08-11'
collected: '2026-08-13'
category: Agent
direction: Agent服务 · GPU控制流性能优化
tags:
- LLM Agent
- GPU Serving
- Batch Scheduling
- Control Flow Optimization
- CUDA
one_liner: 提出Ready Cohort边界模型量化Agent控制流GPU加速潜力，验证设备驻留决策的性能收益
practical_value: '- 高并发Agent服务（如电商智能客服、推荐Agent集群）可将纯确定性控制决策逻辑放在GPU端执行，避免Host往返，控制流速度可提升1.19~2.39倍

  - Agent控制流调度替换固定时间窗口为滑动deadline动态打包策略，可回收81.8%的固定窗口浪费的可加速机会

  - 上线GPU控制流前先测试业务场景的最小盈利batch阈值K，低并发/短调度窗口场景无GPU加速收益，直接用CPU成本更低

  - 多租户Agent推荐/广告调度服务可做集群级控制流全局聚合，凑够batch阈值再下发GPU执行，降低GPU空置率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent服务的控制流（路由选择、状态更新、工具调度）频繁跨CPU-GPU边界，Host调度成为全链路性能瓶颈，且行业缺乏可量化的方法判断控制流是否适合卸载到GPU执行，也没有明确的Host往返开销量化结果，导致Agent服务系统优化缺乏数据支撑。

### 方法关键点
- 定义4个边界量化指标：固定窗口可加速占比F、离线最优可加速占比P⋆、理论上限U、在线实际可加速占比A，明确GPU控制流的可行边界
- 设计等相对deadline场景下的专用动态规划算法，可离线计算P⋆作为调度策略的理论天花板
- 两组对照实验：公开Agent trace静态回放验证动态打包收益；CUDA实现设备驻留决策与Host往返的性能对比，补充负对照排除纯设备启动的干扰

### 关键实验
- 基于Exgentic公开Agent trace的851个会话（覆盖航空、零售、电信场景），泊松回放模拟10万活跃会话，在K=256、50ms调度窗口下，固定窗口F=30.19%，离线最优P⋆=43.00%，动态打包回收81.83%的固定窗口损失机会
- 跨4种GPU硬件（GTX 1660 Ti、L4、H100 SXM5等）的36组配置下，设备驻留决策比Host往返路径快1.19×~2.39×；纯嵌套设备启动（不减少Host决策）的负对照反而慢1.07×~1.99×

### 核心结论
LLM Agent控制流上GPU需要同时通过两道门：一是有足够多同组任务在deadline前凑够最小盈利batch，二是避免不必要的Host决策往返，缺任意一个都不如直接用CPU。
