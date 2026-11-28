---
title: Simulator-as-Proxy World Model for Robot Manipulation
title_zh: 面向机器人操作的模拟器作为代理的世界模型
authors:
- Tingting Liao
- Mingjia Huo
- Hao Li
- Zhengzhong Liu
- Eric P. Xing
- Guangyi Liu
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- University of California, San Diego
- Pinscreen
arxiv_id: '2611.32786'
url: https://arxiv.org/abs/2611.32786
pdf_url: https://arxiv.org/pdf/2611.32786
published: '2026-11-23'
collected: '2026-11-28'
category: Other
direction: 机器人操作 · 世界模型构建与验证
tags:
- World_Model
- Robot_Manipulation
- Simulator
- Video_Generation
- State_Alignment
one_liner: 提出无训练参数的规则模拟+视频渲染的SimPWM框架，可验证机器人世界模型对代理场景的遵循度
practical_value: '- 做电商具身Agent、AR试穿、虚拟导购等场景的动作验证时，可借鉴「无参数规则模拟器+生成模型渲染」的架构，无需大量训练即可保证动作逻辑合规，降低落地成本

  - 多模块协作的生成系统（比如商品演示视频自动生成、虚拟货架互动内容生成）中，可引入显式状态记录模块，对比生成结果与预设状态的一致性，快速定位错误

  - 做生成模型效果校验时，可借鉴扰动测试法，主动修改输入模块的状态参数，验证生成模型对约束的遵循度，筛选更可控的基础模型'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有机器人动作条件视频世界模型默认生成内容与场景代理状态一致，但缺乏可验证该假设的、状态明确可扰动的代理工具。
### 方法关键点
提出SimPWM框架：仅输入首帧与校准相机参数，用3D模型表征机器人、3D点云表征可接触物体，通过无训练参数的规则模拟器执行动作生成状态，对接基础视频模型渲染真实视频，同时输出显式模拟状态，支持扰动测试校验模型对代理状态的遵循度。
### 关键结果
- 三类基础视频模型搭配SimPWM的机器人IoU达0.75-0.78，远超端到端模型的最高0.69
- 引入模拟物体模块后，漏捡率从54%降至38%
- 刚性物体扰动测试中，经仿真-真实对齐数据微调的MiniMax-H3升举率从42%降至10%，验证其对模拟状态的高遵循度
