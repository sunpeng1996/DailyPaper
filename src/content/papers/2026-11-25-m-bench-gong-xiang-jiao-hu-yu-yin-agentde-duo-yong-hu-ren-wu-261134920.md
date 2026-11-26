---
title: '$μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice
  Agents'
title_zh: μ-Bench：共享交互语音Agent的多用户任务完成评测基准
authors:
- Qihao Lin
- Guanxu Chen
- Shuhang Zheng
- Xiaoya Lu
- Jingyi Yang
- Terumi Chiba
- Wenyi Yu
- Chao Zhang
- Zhuan Shi
- Jing Shao
affiliations:
- 上海人工智能实验室
- 上海交通大学
- 中国科学院大学
- 复旦大学
- 清华大学
arxiv_id: '2611.34920'
url: https://arxiv.org/abs/2611.34920
pdf_url: https://arxiv.org/pdf/2611.34920
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: Agent · 多用户语音交互评测
tags:
- Voice Agent
- Multi-User Interaction
- Benchmark
- Full-Duplex
- Task Completion
one_liner: 构建首个共享全双工语音Agent闭环多用户任务完成基准，含800个场景与ATC诊断框架
practical_value: '- 做家庭/车载/线下门店等共享场景语音Agent的团队，可直接复用ATC（Attribution/Threading/Coordination）诊断框架定位多用户交互失败根因，无需从零设计评估维度

  - 多用户交互模拟可借鉴其隔离式用户Profile+仅基于可感知历史生成响应的逻辑，比固定脚本更贴合真实用户动态反馈特性

  - 多用户任务评估可参考JTS（Joint Task Success）+ Pure JTS指标设计，既要覆盖所有用户目标/隐私约束，还要校验工具调用权限合规性，避免结果虚高

  - 自研场景化多用户语音Agent时，可优先序列化重叠语音、补充说话人身份元数据，能快速提升30%+的任务成功率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有语音Agent评测多针对单用户，或仅测试轮次切换、静态预录对话，无法覆盖共享空间下多用户目标冲突、权限差异、语音重叠、交互动态反馈的真实场景，导致评测结果和实际落地表现差距大，亟需能闭环验证多用户联合任务完成效果的基准。

### 方法关键点
- 闭环多用户模拟器：每个用户拥有独立的目标、权限、隐私Profile，仅基于自身可听到的公开对话动态生成响应，而非重放固定脚本
- 场景库覆盖20个领域共100个基础场景，通过人群规模、声学复杂度、follow-up要求三个维度因子组合生成800个评测用例，分工具增强（408个）、无工具（392个）双赛道
- 核心指标JTS要求所有用户目标、隐私约束、终态要求同时满足，新增Pure JTS排除未经授权工具调用的虚高成功；配套ATC诊断框架从归因、线程、协调三个维度定位失败根因

### 关键结果
评测13款语音Agent，头部闭源系统无工具赛道JTS最高62.24%、工具增强赛道最高65.44%，而开源模型无工具赛道JTS普遍低于20%，最高仅19.39%；开源模型主要短板为多轮归因和线程维护，用户规模从2-3人扩大到4-7人时，所有系统JTS平均下降20%+；对MiniCPM-o 4.5做辅助实验，序列化重叠语音+补充身份/语义元数据后JTS相对提升61.84%，但仍有68.62%会话因多用户规划问题失败。

**最值得记住的一句话**：多用户场景下仅测权限合规（Coordination）会严重高估Agent能力，必须结合多线程维护（Threading）和全局JTS指标才能反映真实落地效果。
