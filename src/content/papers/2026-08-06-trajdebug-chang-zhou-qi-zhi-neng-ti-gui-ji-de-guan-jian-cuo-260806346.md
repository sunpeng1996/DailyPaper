---
title: 'TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon
  Agent Trajectories'
title_zh: TRAJDEBUG：长周期智能体轨迹的关键错误定位框架
authors:
- Yunjia Qi
- Zehua Yin
- Xintong Shi
- Hao Peng
- Songyuanyi Lu
- Yixian Liu
- Richeng Xuan
- Yuhong Liu
- Zhichao Hu
- Xiaozhi Wang
affiliations:
- 清华大学
- 清华大学深圳国际研究生院
- 腾讯混元
arxiv_id: '2608.06346'
url: https://arxiv.org/abs/2608.06346
pdf_url: https://arxiv.org/pdf/2608.06346
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: Agent 长轨迹故障诊断与归因
tags:
- Agent Debugging
- Long-horizon Reasoning
- Error Attribution
- Benchmark
- Failure Analysis
one_liner: 基于错误生命周期追踪的长轨迹Agent关键故障定位方案，配套标注基准可直接支撑Agent迭代
practical_value: '- 电商多轮导购、长路径搜索助手等长交互Agent的故障排查，可复用多粒度上下文压缩+证据锚定的错误触发检测逻辑，避免长上下文下漏判关键错误

  - Agent迭代优化可借鉴错误生命周期分类逻辑，过滤已修复/无实际影响的局部错误，仅将最终导致失败的关键错误加入经验库，减少无效反馈干扰

  - 业务失败轨迹复盘可参考其三级归因流程：错误触发检测→错误状态分类→候选集因果归因，大幅降低人工排查成本

  - 构建业务场景自定义Agent评估基准时，可复用TRAJERRBENCH的「证据锚定+多数投票」标注协议，提升标注一致性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
基于LLM的长周期Agent（工具调用、代码生成、多轮客服等）普遍存在错误级联问题，现有故障定位方法在长轨迹下精度骤降，且无法区分多个共存的局部错误中哪些是真正导致最终失败的关键错误，难以支撑Agent效果迭代。

### 方法关键点
- 多粒度轨迹压缩：为每个步骤生成高/中/低三个精度的上下文视图，错误检测时按需调取，既保留局部验证所需的细粒度证据，又降低长上下文处理负担
- 证据锚定的错误触发检测：要求每个疑似错误必须匹配显式可溯源的冲突证据（任务指令冲突/历史上下文冲突/当前步骤自冲突/环境异常），无明确证据的疑似错误直接过滤，避免幻觉误判
- 错误生命周期追踪：将同一冲突来源的错误触发聚合为错误实例，按「是否修复」「是否留下终端影响」分为4类状态，仅保留有终端影响的候选错误进入最终因果归因，过滤无价值的局部错误

### 关键结果
构建含486条人工标注失败轨迹的TRAJERRBENCH基准（覆盖工具调用、代码场景，最长单轨迹平均119.7步），在7个公开基准上对比7种前沿LLM直接Prompt、3种多Agent诊断基线：TRAJDEBUG平均精度34.11%，比同backbone直接Prompt高8.42个点；长轨迹（>140步）下精度仍保持20%以上，比最优基线高6个点；应用到Agent优化时，单轨迹修复平均提升成功率10.8%，历史失败经验跨任务迁移平均提升成功率5.7%。

### 核心结论
长轨迹Agent故障定位的核心不是找出所有局部错误，而是定位到最早的、未被修复、最终影响任务结果的决定性错误。
