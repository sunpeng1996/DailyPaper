---
title: 'OpenGCUA: Toward a Fully Open Stack for Generalist Computer Use'
title_zh: OpenGCUA：面向通用计算机使用Agent的全开源技术栈
authors:
- Hanzhang Zhou
- Long Li
- Quyu Kong
- Lei Wang
- Panrong Tong
- Long Chen
- Tianyu Xia
- Gongjie Zhang
- Xu Zhang
- Chen Liu
affiliations:
- Alibaba Group
arxiv_id: '2610.22200'
url: https://arxiv.org/abs/2610.22200
pdf_url: https://arxiv.org/pdf/2610.22200
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: 通用计算机使用Agent 全栈开源方案
tags:
- Computer_Use_Agent
- Open_Source_Stack
- Code_Execution
- Harness_Optimization
- Cross_Device_SDK
one_liner: 开源通用计算机使用Agent全栈，支持代码执行与决策下放，8款大模型任务得分平均提升19.6分
practical_value: '- 开发电商运营RPA类Agent时，可复用代码执行设计：将GUI操作、CLI命令、API调用封装为统一Python编程接口，支持循环/条件判断，减少大模型调用次数，降低交互延迟

  - Agent调度框架可借鉴harness-to-model决策转移思路：将截图请求、任务状态跟踪等规则固化的逻辑下放给大模型自主决策，可提升KV缓存命中率10+百分点，降低推理成本

  - 多端Agent开发可直接复用其跨设备SDK：统一PC、浏览器、手机的控制接口，支撑跨设备的电商运营、用户服务类Agent任务开发

  - 模型选型时可参考其资源-性能曲线结论：低资源场景下优先选择高性价比小模型，高要求场景再切换到大模型，平衡任务效果与成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
前沿通用计算机使用Agent（如GPT-6 Astra交互系统）全链路闭源，限制了架构设计的研究与落地；现有GUI-only Agent交互效率低，无法灵活结合可视化与程序化接口完成复杂任务，且基准测试环境与真实设备存在明显Gap，落地性差。
### 方法关键点
- 引入代码执行核心设计：将GUI操作、CLI命令、API调用统一封装为Python可执行接口，支持循环、条件判断等控制流，单模型调用即可完成多步组合操作
- 提出harness-to-model决策转移：将原本由调度框架固化的规则（如每步强制截图、上下文保留策略）下放给大模型自主决策，支持按需请求截图、自主跟踪任务状态
- 开源真实设备调度框架与跨设备SDK：解决基准环境未覆盖的真实设备挑战（如多窗口共享、用户并发操作），统一PC、浏览器、移动端的控制接口
### 关键结果
在OSWorld-v2离线82任务集上，对比支持批量GUI操作的基线，OpenGCUA使8款前沿大模型平均部分任务得分提升19.6分，单任务步骤平均减少53%，平均输出Token减少27.2%；按需截图机制可使KV缓存命中率提升10.5~14.4个百分点；真实macOS设备上Qwen3.8-Max的推理Token消耗是GPT-6 Astra的19.4倍，不同模型真实设备执行效率差距显著。
### 核心结论
代码执行是计算机使用Agent从批量动作升级到灵活执行的核心路径，资源约束下的模型选择比单纯追高基准得分更具业务价值
