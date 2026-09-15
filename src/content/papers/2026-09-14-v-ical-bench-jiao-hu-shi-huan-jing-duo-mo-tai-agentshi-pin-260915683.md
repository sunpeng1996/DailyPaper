---
title: 'V-ICAL Bench: Evaluating Video In-Context Learning for Multimodal Agents in
  Interactive Environments'
title_zh: V-ICAL Bench：交互式环境多模态Agent视频上下文学习评估基准
authors:
- Ziqian Fan
- Shibo Xu
- Junjie Li
- Xiangyu Zhao
- Shengyuan Ding
- Yifan Yang
- Zhenjie Yang
- Haodong Duan
- Yue Zhou
- Zhihang Zhong
affiliations:
- Shanghai Jiao Tong University
- South China University of Technology
- Fudan University
- Microsoft Research Asia
- The University of Hong Kong
arxiv_id: '2609.15683'
url: https://arxiv.org/abs/2609.15683
pdf_url: https://arxiv.org/pdf/2609.15683
published: '2026-09-14'
collected: '2026-09-15'
category: Agent
direction: 多模态Agent · 视频ICL能力评估
tags:
- Multimodal Agent
- In-Context Learning
- Video Understanding
- Benchmark
- Interactive Environment
one_liner: 推出覆盖37类环境342个任务的多模态Agent视频ICL评估基准，量化当前模型与人类能力的差距
practical_value: '- 做视频引导的交互Agent（如电商直播导购Agent、操作指引Agent）时，可复用四阶段决策故障归因框架（知识归纳→状态
  grounding→规划→动作提交）定位能力短板，优先优化策略迁移而非规则迁移模块

  - 多模态Prompt设计可参考模态适配原则：刚性约束/离散逻辑用明文规则描述，动态行为/操作细节用视频演示传递，同时避免冗余视频演示覆盖实时交互反馈导致决策偏差

  - 评估交互类多模态Agent时，可复用双指标体系：用通过率度量任务完成能力，归一化得分度量部分进度，同时引入动态环境、记忆依赖任务的专项测试维度

  - 电商场景的新手操作引导、直播带货话术动作模仿类Agent，可参考任务构造方法，用少量人类演示视频作为ICL样本，替代大量标注的微调数据集降低成本'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有多模态ICL评估多局限于静态离线范式，仅测试被动语义理解，无法衡量Agent从视频演示中归纳策略、在动态交互环境中闭环执行的真实能力，缺少覆盖全决策链路的系统性评估基准。
### 方法关键点
- 覆盖7类环境家族、37种环境、342个标注任务，包含静态/动态环境、单帧/多帧记忆依赖任务，覆盖导航、射击、控制等多类交互场景
- 任务仅提供1-4个人类 curated 演示视频+最小必要文本规则作为ICL输入，要求Agent在无参数更新、无额外干预的条件下完成多轮闭环交互
- 采用双指标评估体系：通过率衡量任务完成能力，归一化到0-100的最终得分衡量部分进度，同时新增细粒度轨迹审计框架，从规则/策略迁移、四阶段决策链路两个维度定位故障点
### 关键实验结果
测试19个SOTA多模态模型，最佳模型Seed-2.1-Pro仅得54.4/100，远低于人类基线83.6/100；开源模型最佳DeepSeek-V4.1-Flash仅得34.8/100；动态环境下模型平均得分下降42.3%，多帧记忆任务下得分下降32.6%，远高于人类对应降幅20.2%、17.4%；细粒度审计显示模型策略迁移成功率（最高31.7%）远低于规则迁移成功率（最高84.3%），核心瓶颈集中在状态 grounding 与规划阶段。
### 核心结论
当前多模态模型的视频ICL能力仍存在巨大缺口，将视频演示转化为可执行闭环策略的能力远未达到可用水平，动态环境适配与视觉记忆是优先级最高的优化方向
