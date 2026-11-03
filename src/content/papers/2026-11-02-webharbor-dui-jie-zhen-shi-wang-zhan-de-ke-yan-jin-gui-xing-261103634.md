---
title: 'WebHarbor: Docking Real Websites for Evolving GUI Agent Environments'
title_zh: WebHarbor：对接真实网站的可演进GUI Agent执行环境集
authors:
- Zhaoyang Wang
- Qianhui Wu
- Boyu Gou
- Demi Wang
- Jiacheng Zhang
- Peichun Hua
- Qize Li
- Shi Qiu
- Yifan Jiang
- Yifan Zhang
affiliations:
- University of North Carolina at Chapel Hill
- Microsoft
- The Ohio State University
- Carnegie Mellon University
- University of Michigan
arxiv_id: '2611.03634'
url: https://arxiv.org/abs/2611.03634
pdf_url: https://arxiv.org/pdf/2611.03634
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: GUI Agent 评测训练环境构建
tags:
- GUI_Agent
- Web_Agent
- RL_Training
- Benchmark
- Synthetic_Environment
one_liner: 提供153个Docker化真实网站镜像与3518个任务，支撑GUI Agent的稳定评测与RL训练
practical_value: '- 构建业务场景的Agent评测环境时可复用任务驱动的人-Agent协作流水线：先由任务圈定功能范围，编码Agent实现环境，人工仅做保真度、功能正确性校验，大幅降低环境构建成本

  - 做电商/广告类Web Agent的RL训练时，可基于WebHarbor的153个真实网站镜像快速搭建离线训练环境，避免真实网站反爬、内容漂移导致的训练不稳定问题

  - 跨环境Agent泛化性验证可参考其实验结论：在高保真离线合成环境训练的4B级小参数GUI Agent，泛化到真实网站任务的表现优于在真实网站直接做RL训练的同规模Agent'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
GUI Web Agent评测依赖稳定可复现的环境，现有真实网站评测存在内容变动、反爬限制、鉴权流程覆盖不足的问题，38%的在线任务会被反爬拦截，22%的任务因网站改版失效；而合成环境普遍存在功能深度不足、视觉保真度低的问题，同时支持离线执行、富图片内容、登录态流程的环境缺失，严重制约Agent的可靠评测与大规模RL训练。

### 方法关键点
- 采用任务驱动的环境构建范式：先由目标任务圈定需要复现的页面、交互流程、数据范围，避免全量复刻真实网站的冗余成本
- 人-Agent协作流水线：编码Agent基于真实网站的渲染DOM、资源路径实现全栈环境，人工仅校验视觉保真度、功能正确性、任务有效性，迭代修复缺陷
- 产出153个Docker化可执行网站环境，支持快速重置、鉴权流程、状态持久化，覆盖3518个多步骤、登录后操作任务

### 关键结果
- 对比同规模SOTA开源Web Agent OpenWebRL-4B，基于WebHarbor训练的WebHarbor-4B在WebVoyager、Online-Mind2Web两个真实网站基准上平均得分75.8，超出基线5.2个百分点，是当前最优开源Web Agent
- 环境评测的模型排序与真实网站基准的Spearman相关系数达1.0，可完全替代真实网站做Agent能力评测
- 4B级小模型在WebHarbor训练后，鉴权类任务成功率提升13.3个百分点，交易预订类任务成功率提升21.4个百分点

### 核心结论
高保真、任务对齐的离线合成环境，完全可以支撑GUI Agent的RL训练，效果甚至优于在不稳定的真实网站做训练
