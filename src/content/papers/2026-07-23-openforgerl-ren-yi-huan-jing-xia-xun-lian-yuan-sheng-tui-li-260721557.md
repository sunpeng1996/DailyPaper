---
title: 'OpenForgeRL: Train Harness-native Agents in Any Environment'
title_zh: OpenForgeRL：任意环境下训练原生推理Harness智能体的开源框架
authors:
- Xiao Yu
- Baolin Peng
- Ruize Xu
- Hao Zou
- Qianhui Wu
- Hao Cheng
- Wenlin Yao
- Nikhil Singh
- Zhou Yu
- Jianfeng Gao
affiliations:
- Columbia University
- Dartmouth College
- Microsoft Research
arxiv_id: '2607.21557'
url: https://arxiv.org/abs/2607.21557
pdf_url: https://arxiv.org/pdf/2607.21557
published: '2026-07-23'
collected: '2026-07-24'
category: Agent
direction: Agent端到端RL训练基础设施
tags:
- Agent
- RL
- Harness
- Training
- GUI
one_liner: 开源框架实现任意推理Harness+任意环境下的Agent端到端RL训练
practical_value: '- 业务侧开发带工具调用的Agent（电商客服、商家运营工具Agent、内容审核Agent）时，可复用Proxy+K8s编排架构，解耦RL训练和Harness推理，彻底避免训练部署不一致的性能损耗

  - 低资源Agent训练场景可复用其全自动任务合成流水线，仅需数千级高质量任务即可超过同规模基线效果，大幅降低标注成本

  - 工程上训练有环境依赖的Agent（如浏览器操作的商品上架Agent、数据查询Agent）时，可直接复用远程容器rollout+超时/错误处理方案，避免训练节点被复杂环境依赖占用资源

  - 多Harness训练的结论可复用：同时在多个业务常用Harness上训练能提升跨场景泛化性，RL可有效提升Agent自校验、工具覆盖等可靠性能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前SOTA Agent普遍依赖Claude Code、OpenClaw等复杂推理Harness实现多轮交互、工具调用和外部系统对接，但现有开源SFT/RL训练栈无法原生支持Harness的有状态、多进程推理逻辑：要么为适配训练简化Harness实现，导致训练部署不一致；要么无法规模化运行容器化的Harness环境，使得开源Agent训练和闭源方案差距持续拉大。
### 方法关键点
- 轻量Proxy层拦截所有Harness的模型调用请求，自动重建完整训练轨迹，无缝对接veRL等标准RL训练框架，无需修改原有Harness逻辑
- 基于K8s的编排器将每个rollout调度到独立远程容器运行，弹性扩缩容，完全解耦训练GPU资源和推理/环境运行的CPU资源
- 配套全自动任务合成流水线，支持工具调用、GUI操作等多场景的SFT/RL任务自动生成、校验，解决低资源场景数据不足问题
### 关键结果
- 工具调用Claw场景：30B MoE模型仅用千级训练任务，ClawEval pass3达31.7、pass@3达55.9，QwenClawBench达33.7，全部优于同规模开源基线
- GUI Agent场景：8B VLM模型OSWorld-Verified达37.7、Online-Mind2Web达63.0、WebVoyager达72.3，超过同规模基线，部分指标追平数倍参数的大模型
### 核心结论
Agent训练必须和实际部署的Harness、环境完全对齐才能最大化落地效果，RL对Agent可靠性的提升效果显著优于仅靠SFT
