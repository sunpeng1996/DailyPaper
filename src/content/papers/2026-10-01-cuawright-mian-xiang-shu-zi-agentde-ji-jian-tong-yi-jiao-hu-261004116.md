---
title: 'CUAWright: A Minimal Unified Interface for Digital Agents'
title_zh: CUAWright：面向数字Agent的极简统一交互接口
authors:
- Yadong Lu
- Theodore Lee
- Yifei Li
- Lawrence Keunho Jang
- Tianci Xue
- Yu Su
- Huan Sun
- Ahmed Hassan Awadallah
affiliations:
- Microsoft Research
- National University of Singapore
- The Ohio State University
- Carnegie Mellon University
arxiv_id: '2610.04116'
url: https://arxiv.org/abs/2610.04116
pdf_url: https://arxiv.org/pdf/2610.04116
published: '2026-10-01'
collected: '2026-10-06'
category: Agent
direction: Agent 执行层交互架构优化
tags:
- Computer Use Agent
- Terminal Interface
- Harness Design
- Dynamic Tool Construction
- File System Memory
one_liner: 提出仅3K行代码的终端原生数字Agent框架，以bash为唯一动作接口，性能成本优于GUI/混合架构
practical_value: '- 电商运营自动化Agent可复用终端优先设计思路，优先用CLI/API调用替代GUI模拟操作，长流程任务成功率可提升30%+同时降低调用成本

  - 长周期Agent记忆管理可借鉴文件系统作为持久工作区的方案，无需额外开发记忆模块，直接通过文件读写存储中间结果、自定义工具，大幅降低架构复杂度

  - 多Agent架构选型可参考其ablation结论：当前前沿大模型本身具备自校验能力，单Agent在多数终端可执行任务上性能不输多Agent，还能减少交互轮次降低成本

  - Agent成本优化可借鉴按需拉取视觉信息的设计，默认仅用文本观测，仅必要时调用截图工具，可降低30%+的多模态token消耗'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有计算机使用Agent普遍绑定GUI或领域专用静态工具集，无法直接对系统状态做编程操作，也不能灵活构造工具，导致长流程任务成功率低、调用成本高，亟需更通用高效的交互架构。

### 方法关键点
- 仅3K行代码的极简终端原生harness，以bash命令作为唯一动作接口，覆盖系统操作、GUI控制（通过xdotool等CLI工具调用）、代码执行全场景
- 默认观测为终端文本输出，仅按需调用截图工具加载视觉信息，大幅降低多模态token消耗
- 以文件系统作为持久工作区，无需额外记忆模块，Agent可直接通过读写文件存储中间结果、管理上下文，还能动态编写、测试、复用自定义工具

### 关键实验
覆盖网页、桌面、CAD共6个基准测试集，同模型下对比GUI/混合架构baseline：长流程网页任务Odysseys上成功率提升44.0%，Online-Mind2Web上成功率提升4.7%；桌面任务OSWorld 2.0上，GPT-5.5版本partial reward相对提升33.2%，单任务成本降低37.5%；CAD任务BenchCAD上IoU相对提升41.6%，WeaveBench通过率提升18.4%。 ablation实验显示禁用文件系统编程操作后，GPT-5.6 Sol版本性能下降12.1个百分点，单Agent性能与多Agent持平但交互轮次更少。

**最值得记住的结论**：数字环境的可编程性远高于其GUI界面呈现的程度，以终端为核心的极简交互框架是提升数字Agent性能与效率的核心路径。
