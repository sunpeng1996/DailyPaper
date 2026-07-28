---
title: 'StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents'
title_zh: StateAct：面向长周期计算机操作Agent的程序状态优先架构
authors:
- Yan Yang
- Xiangru Jian
- Ziyang Luo
- Zirui Zhao
- Yutong Dai
- Ziji Shi
- Hanshu Yan
- Jun Hao Liew
- Silvio Savarese
- Junnan Li
affiliations:
- Salesforce AI Research
arxiv_id: '2607.22798'
url: https://arxiv.org/abs/2607.22798
pdf_url: https://arxiv.org/pdf/2607.22798
published: '2026-07-23'
collected: '2026-07-28'
category: Agent
direction: 长周期桌面操作Agent · 状态感知优化
tags:
- Computer-Use Agent
- Multi-Agent
- State Grounding
- Long-Horizon Task
- Agent Verification
one_liner: 提出程序状态优先的多Agent架构，提升长周期桌面操作Agent准确率的同时降本9倍
practical_value: '- 可复用「主逻辑优先操作底层数据/状态+仅必要时调用视觉/界面交互子Agent」的架构，降低长任务的感知误差和token成本，比如电商运营Agent处理后台订单、商品数据时优先调用API读写，仅特殊弹窗等场景调用GUI操作

  - 独立状态校验的设计可直接迁移到Agent验收环节：不读取Agent的执行叙事，直接校验最终落地的真实数据（如商品上下架状态、订单修改结果），避免自验证的一致性偏差

  - 长任务上下文管理的三个trick：子任务用独立上下文执行、旧上下文自动压缩、核心计划外置可复用，能有效缓解LLM长上下文遗忘问题，降低token消耗'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有计算机操作Agent大多基于屏幕像素感知做决策，但像素是程序状态的有损渲染，不同状态可能对应同一张截图，长周期任务中感知误差会不断累积，同时基于像素的自验证也无法准确判断任务最终是否完成，成本高、准确率低。

### 方法关键点
- 主Agent仅操作程序底层状态（文件、DOM、数据库、Shell等），不直接暴露GUI操作权限，仅当子目标不可避免需要视觉交互时（如非脚本化弹窗、画布拖拽）才调用专用GUI子Agent，实测仅1.1%的主Agent步骤需要调用GUI
- 独立的Finish Gate校验模块：仅接收原始任务指令，不读取主Agent的执行轨迹、计划等信息，直接查询持久化的程序状态做验收，最多支持3轮重试
- 长上下文管理：子任务独立上下文执行返回精简结果、接近上下文上限时自动压缩旧前缀、核心计划外置每轮重新注入，避免长任务上下文溢出和遗忘

### 关键实验
在OSWorld 2.0长周期桌面操作基准（108个任务）上，基于Claude Opus 4.8 backbone，对比纯像素驱动的基线：二进制准确率从20.6%提升到26.9%，部分准确率从54.8%提升到61.6%；单任务成本从~$72降到~$7.8，成本降低约9倍；纯代码无GUI的变体仅能达到45.9%的部分准确率，低于基线；短任务基准上和基线性能无显著差异，证明状态优先的优势集中在长周期任务场景。

**最值得记住的一句话**：状态优先的设计把长周期Agent的瓶颈从感知移到了推理，现在的核心问题是Agent「想的对不对」，而不是「看的对不对」。
