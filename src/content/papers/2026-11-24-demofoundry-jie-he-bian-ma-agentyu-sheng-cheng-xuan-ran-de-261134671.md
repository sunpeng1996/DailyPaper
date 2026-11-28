---
title: 'DemoFoundry: Toward Scalable Photorealistic Robot Data with Coding Agents
  and Generative Rendering'
title_zh: DemoFoundry：结合编码Agent与生成渲染的可扩展高保真机器人数据框架
authors:
- Ruixiang Wang
- Xinyue Yao
- Xuanning Zhou
- Yueci Deng
- Yongyi Su
- Kui Jia
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- DexForce Technology Co., Ltd.
- Foshan University
arxiv_id: '2611.34671'
url: https://arxiv.org/abs/2611.34671
pdf_url: https://arxiv.org/pdf/2611.34671
published: '2026-11-24'
collected: '2026-11-28'
category: Agent
direction: Agent 仿真训练数据自动生成
tags:
- Coding Agent
- Generative Rendering
- Robot Learning
- Data Synthesis
- Simulation-to-Real
one_liner: 结合编码Agent与生成渲染自动生成高保真、物理一致的机器人训练演示数据
practical_value: '- 可复用「Agent自动生成结构化标注+生成模型做域适配」的架构，解决推荐/广告场景稀缺样本标注成本高、模拟数据与真实分布有gap的问题

  - 可借鉴自动校验筛选成功样本的机制，在生成式推荐/LLM内容生成链路中加入自动化校验环节，过滤低质量样本，降低人工审核成本

  - 编码Agent自动编写交互程序生成样本的思路，可迁移到多场景下模拟用户行为、生成用户-物品交互训练数据，补足冷启动场景样本缺口'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
机器人大规模训练需要同时具备真实视觉观测和对齐动作标注的演示数据，传统仿真合成数据存在显著视觉域gap，纯视频生成方案难以保证物理交互一致性，也无法提供对齐的动作标签。
### 方法关键点
1. 耦合编码Agent与生成渲染：编码Agent基于现有机器人片段构建真实-代理视频对训练渲染器，同时根据场景参考和任务指令自动重建任务相关几何、编写可执行控制程序，无需目标任务的人工演示；
2. 物理模拟器执行程序生成带对齐机器人状态、动作的代理视频，再由渲染器转换为场景一致的高保真观测数据，无需逐场景做精细化外观建模；
3. 加入自动化任务执行校验环节，筛选成功轨迹用于后续渲染和策略训练。
### 关键结果
生成数据的视觉质量、动作-视频一致性显著提升，基于生成数据训练的策略性能优于原始仿真训练，接近同等数量真实演示数据训练的性能。
