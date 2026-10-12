---
title: Proactive Agentic Orchestration
title_zh: PORCHESTRA：支持子代理主动反馈的Agent编排框架与训练方法
authors:
- Xueyang Feng
- Chaozhuo Li
- Xiaohe Bo
- Jiakai Tang
- Chenxi Li
- Qiwei Ye
- Xu Chen
affiliations:
- Renmin University of China
- The Chinese University of Hong Kong Shenzhen
- Beijing Academy of Artificial Intelligence
arxiv_id: '2610.13485'
url: https://arxiv.org/abs/2610.13485
pdf_url: https://arxiv.org/pdf/2610.13485
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: 多Agent编排 · 动态长周期任务优化
tags:
- Agent-Orchestration
- Multi-Agent
- Self-Distillation
- Long-Horizon-Task
- Dynamic-Environment
one_liner: 提出支持子代理主动调整配置的Agent编排框架及自蒸馏训练方法，长周期任务成功率平均提升9.1%
practical_value: '- 电商客服、售后等长周期多步Agent任务可复用主动反馈机制：允许子任务执行Agent在遇到工具不可用、需求歧义时主动向上层编排器请求调整工具集/子目标，避免无效重试降低成本，提升任务完成率

  - 小参数编排Agent可复用OPOD自蒸馏训练范式：结合子Agent执行过程反馈的过程监督与最终任务结果的结果监督，无需额外大模型打分，就能低成本提升小编排Agent的决策准确率

  - 多Agent协作协议可复用结构化主动通信设计：固定「状态描述+调整请求+证据支撑」的通信格式，降低跨Agent交互的理解误差，减少通信开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent编排方法存在两个核心痛点：一是执行阶段子代理的目标、工具集等配置在创建时固定，遇到环境动态变化（比如工具失效、任务目标变更）时只能等执行结束或预设触发条件才调整，延迟高、无效步骤多；二是优化阶段只有稀疏延迟的最终任务反馈，难以归因到单个编排决策，优化效率低，无法适配电商售后、深度调研等动态长周期场景需求。

### 方法关键点
- 提出PORCHESTRA主动编排范式：允许子代理在执行任意逻辑节点暂停，通过「状态+请求+证据」的结构化协议向编排器请求调整子目标、上下文、工具集、执行预算，调整后保留本地执行上下文继续执行，无需销毁重建子代理
- 配套OPOD on-policy编排蒸馏训练方法：将子代理的主动反馈归因到历史编排决策，生成自然语言形式的改进提示，作为过程监督信号结合最终任务奖励的RWR损失，通过自蒸馏方式优化编排器策略，无需额外标注数据

### 关键实验
在GAIA、GAIA2、SWE-Bench三个长周期动态任务基准上测试，对比ReAct、AORCHESTRA等7个基线：推理阶段PORCHESTRA相比最强基线任务成功率平均提升9.1%，在动态性最高的GAIA2基准上相对提升24.6%，同时API成本降低36%；训练阶段结合OPOD的小参数Qwen3.5-9B编排器相比现有训练基线成功率平均提升10.0%，达到Pareto最优性价比。

最值得记住的一句话：让一线执行的子代理主动反馈问题，而非靠编排器事后感知调整，是提升动态长周期多Agent系统效率的核心路径
