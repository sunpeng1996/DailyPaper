---
title: 'DeskForge: Dense Supervision from Desktop Environments for Computer-Use Agents'
title_zh: DeskForge：可控桌面环境生成稠密监督数据训练计算机操作Agent
authors:
- A. Said Gurbuz
- Ahmed Nassar
- Sunghwan Hong
- Marc Pollefeys
- Peter W. J. Staar
affiliations:
- ETH Zurich
- IBM Research Zurich
- Microsoft
arxiv_id: '2610.02320'
url: https://arxiv.org/abs/2610.02320
pdf_url: https://arxiv.org/pdf/2610.02320
published: '2026-09-30'
collected: '2026-10-07'
category: Agent
direction: 计算机操作Agent · GUI监督数据合成
tags:
- GUI Agent
- Visual Grounding
- Synthetic Dataset
- Vision-Language Model
- Long-horizon Task
one_liner: 提出可控桌面数据生成框架及1.2M稠密标注数据集，大幅提升GUI Agent的grounding与长任务性能
practical_value: '- 做电商/企业内部自动化操作Agent时，可复用可控环境合成数据的思路，定向生成多窗口、遮挡、样式变化等难例样本，替代部分高成本人工标注

  - Agent架构可拆分上层任务planner与下层GUI grounding模块，单独微调grounding模块即可提升全链路任务成功率，无需修改planner逻辑，迭代效率高

  - 用LoRA微调通用/垂直领域VLM做GUI grounding的方案可直接复用，200K量级样本即可获得10%+的精度提升，小算力即可落地

  - 做Web/App界面元素检测/解析时，稠密标注的合成数据可补充真实标注的覆盖缺口，跨平台迁移效果优于纯小样本真实标注训练'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有计算机操作Agent的训练数据多为静态单应用标注，缺乏多窗口重叠、主题样式变化、分辨率差异等复杂桌面场景的稠密监督，无法支撑Agent在真实环境下的鲁棒GUI grounding能力，人工标注这类复杂场景成本极高且覆盖度有限。
### 方法关键点
- 搭建可控Linux桌面环境DeskForge，支持自定义应用组合、窗口布局、主题样式、分辨率，自动生成多样化真实桌面场景
- 融合截图、系统可访问性树、窗口几何信息做稠密标注，覆盖元素位置、可见性、交互属性、层级关系，同时记录点击交互的前后状态转移
- 构建DeskForge-1M数据集，包含1.2M标注桌面样本、159.7M元素实例、917K点击转移，通过VLM自动生成自然语言指令构建grounding训练对
### 关键结果
用LoRA微调4款VLM，相比base模型，Qwen3.5-4B在ScreenSpot-Pro上精度提升11.51pp，OSWorld-G提升10.11pp；固定上层planner仅替换grounding模型，WebArena-Infinity任务完成数从31提升至50，OpenApps从3提升至15。
> 核心结论：仅优化GUI grounding模块即可大幅提升计算机操作Agent的长任务完成率，可控合成的监督数据是降低Agent训练标注成本的核心路径。
