---
title: 'From Watching to Steering: Enabling Human-Coding Agent Collaboration through
  Execution Traces'
title_zh: 从观测到调控：基于执行轨迹的人机协同编码Agent框架
authors:
- Xiaoke Yan
- Jiaying Lei
- Danqing Shi
- Zichen Wang
- Nan Cao
affiliations:
- 同济大学
- 瑞典隆德大学
arxiv_id: '2611.04466'
url: https://arxiv.org/abs/2611.04466
pdf_url: https://arxiv.org/pdf/2611.04466
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: Agent 人机协同执行轨迹优化
tags:
- Coding Agent
- Execution Trace
- Human-in-the-loop
- Skill Distillation
- Interactive Visualization
one_liner: 提出可视化执行轨迹、可细粒度干预、轨迹转技能蒸馏的人机协同编码Agent系统VibeTrace
practical_value: '- 可复用「执行轨迹结构化建模+层级可视化」方案，落地到推荐/广告Agent的运行态可观测平台，快速定位多步推理、工具调用错误，降低排查成本

  - 借鉴轨迹级fork干预机制，解决大模型Agent执行出错需全链路重启的问题，保留已验证的上游执行结果，降低重复计算开销

  - 在线轨迹转技能蒸馏的三阶段流程（经验评估→补丁蒸馏→验证入库）可直接迁移到业务Agent的经验沉淀模块，无需微调基座即可实现能力迭代，适配电商运营、广告投放等高频重复场景

  - 技能池更新的质量&效率双维度打分机制，可避免低质量经验污染知识库，平衡能力提升与执行成本控制'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前编码Agent多采用自主执行黑箱模式，用户仅能获取最终输出或线性日志，无法细粒度观测执行过程、定位错误根源，干预需重启全流程，且人工纠正的经验无法沉淀复用，长周期任务的效率与准确率瓶颈显著。
### 方法关键点
- 结构化执行轨迹提取：将Agent的规划、信息获取、代码修改、工具调用等12类原子动作，按时间顺序、因果依赖封装为带状态、输出、耗时、token消耗的统一轨迹单元
- 交互式轨迹可视化与干预：层级化展示任务→子任务→动作节点的执行链路，高亮失败节点、支持分支对比，用户可对任意历史节点加注释、fork分支重定向执行，无需丢弃已验证的上游结果
- 在线轨迹转技能蒸馏：对用户干预的轨迹先做可复用性、信息价值、安全性三维评估，再蒸馏为包含触发上下文、决策逻辑、执行策略的技能补丁，经质量、效率双维度验证后更新外部技能池，全程不修改基座模型参数
### 关键实验
在SWE-bench Verified数据集上对比无技能基线、无用户反馈的轨迹蒸馏基线，带反馈的轨迹蒸馏方案将任务通过率从65.0%提升至68.0%，输入token降低23.0%，执行成本降低15.5%，执行耗时降低14.5%；20人对照用户研究显示，相较原生日志，轨迹可视化将错误定位准确率从76%提升至95%，平均排查耗时从99.7s缩短至44.0s。
### 核心洞察
人机协同的核心不是让Agent完全替代人，而是通过透明可干预的执行链路、可沉淀的协作经验，把人的一次性干预转化为Agent的长期可复用能力。
