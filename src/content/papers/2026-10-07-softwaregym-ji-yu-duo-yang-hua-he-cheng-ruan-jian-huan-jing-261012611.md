---
title: 'SoftwareGym: Scaling Computer-Use Agent Training with Diverse Synthesized
  Software Environments'
title_zh: SoftwareGym：基于多样化合成软件环境的计算机操作Agent规模化训练框架
authors:
- Tian Jin
- Wenhao Wang
- Jing Kang
- Haoting Shi
- Rui Ye
- Yijun Lu
- Siheng Chen
affiliations:
- Shanghai Jiao Tong University
- Zhejiang University
arxiv_id: '2610.12611'
url: https://arxiv.org/abs/2610.12611
pdf_url: https://arxiv.org/pdf/2610.12611
published: '2026-10-07'
collected: '2026-10-12'
category: Agent
direction: 计算机操作Agent · 训练环境自动化合成
tags:
- Computer-Use Agent
- GUI Agent
- Environment Synthesis
- Agent Training
- Benchmark
one_liner: 提出自动化合成GUI软件环境的多Agent流水线，解决计算机操作Agent训练数据瓶颈
practical_value: '- 开发GUI交互类Agent（如电商后台操作Agent、用户端购物助手Agent）时，可复用其「设计-实现-验证-修复」多Agent流水线自动生成训练环境，大幅降低人工标注与真实环境搭建成本

  - 训练任务生成可借鉴其分层设计思路：先验证单功能可用性，再组合为多步骤复杂任务，同时加入干扰项提升Agent泛化能力，避免过拟合特定界面布局

  - Agent效果评测可参考其Outcome-Driven评估方案：从目标终态倒推初始状态，搭配可编程自动校验逻辑，提升评测效率与结果可复现性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前计算机操作Agent（CUA）训练高度依赖现有软件环境，原生应用集成成本高、易导致Agent过拟合特定软件，浏览器类模拟环境交互深度与工作流复杂度不足，无法同时满足训练环境的多样性、可靠性、可扩展性三大要求，成为CUA规模化训练的核心瓶颈。

### 方法关键点
- 三阶段自动化合成软件环境：设计阶段基于最小人工输入生成功能规范、多样化UI蓝图与SVG资产，通过布局树编辑距离约束保证不同变体的结构差异；实现阶段将设计包转换为可执行应用，先完成源码级功能校验；评估阶段通过GUI测试+迭代修复保障功能可靠性，只有通过双重验证的应用才进入环境库。
- 配套任务合成流程：先提取经过GUI验证的功能点，按「单功能短流程/跨功能多步/长流程组合」分为三类难度，最终生成带明确初始状态、终态校验规则的自然语言任务，避免任务依赖不可用功能。

### 关键实验
共合成12个类别182个可运行应用，平均GUI任务通过率达91.5%；构建包含120个任务的SoftwareGym-Bench评测集；仅用合成环境轨迹训练Qwen3.5-9B模型，在完全未见过的OSWorld基准上Pass@3从41.39%提升到56.97%，在SoftwareGym-Bench上Pass@3达40.0%，超过多个更大参数的专用CUA模型；单个应用平均合成成本仅70.76美元、耗时237分钟，远低于人工开发成本。

### 核心结论
多样化的合成训练环境可以提供跨域可迁移的GUI交互能力，是现有原生软件训练数据的有效补充，能大幅降低CUA的训练落地门槛。
