---
title: Editable Visual Design
title_zh: 基于编码Agent的可编辑视觉设计范式
authors:
- Junyan Ye
- Wei Liu
- Dongzhi Jiang
- Zichen Wen
- HaoDong Li
- Zhutao Lv
- Jiaxin Lin
- Jinhua Yu
- Jun He
- Zilong Huang
affiliations:
- Tencent Hunyuan
- Sun Yat-sen University
- Tsinghua University
- The Chinese University of Hong Kong
- Shanghai Jiao Tong University
arxiv_id: '2609.04034'
url: https://arxiv.org/abs/2609.04034
pdf_url: https://arxiv.org/pdf/2609.04034
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: 编码Agent · 多模态协同视觉生成
tags:
- Coding Agent
- VLM
- Diffusion Model
- Visual Generation
- Human-AI Collaboration
one_liner: 通过VLM创意脑+图像模型模拟器的Agent工作流，产出兼具美学效果与可编辑性的视觉设计
practical_value: '- 电商营销素材自动生成场景可复用「先调用图像模型生成美学参考再写结构化代码」的流程，兼顾视觉效果和可编辑性，解决扩散生成素材无法二次修改的痛点

  - Agent任务调度可借鉴该分工框架：用通用推理大模型做规划、校验、代码生成，用垂直领域模型（如图生图、素材生成模型）做能力补全，降低单一模型的能力瓶颈

  - 可复用「渲染结果+VLM校验+局部代码修复」的闭环自修复机制，落地到页面/素材自动生成的工程链路中，减少人工校验成本

  - 对需要可追溯的生成场景（如营销物料合规审核），可借鉴Agent Design Replay设计，序列化全决策链路，满足审计、人工干预需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有视觉生成路线存在明显短板：扩散类图像模型生成效果好但输出是纠缠位图，文字易出错、无法分层编辑，难以直接用于生产；纯代码生成的视觉方案结构规范、可编辑，但缺乏全局美学直觉，复杂视觉资产生成效果僵硬，无法满足商业设计的视觉要求，亟需兼顾美学效果和工程可编辑性的生成范式。
### 方法关键点
- 采用VLM+图像生成模型的分工协作架构：VLM作为创意脑，负责需求理解、设计规划、代码生成与效果校验；图像生成模型作为视觉模拟器，按需生成全局美学参考图与独立分层的视觉资产
- 执行「先想象后执行」的闭环工作流：先调用图像模型生成理想效果参考，提取色彩、布局、风格作为先验，再按需生成独立带alpha通道的视觉资产，编写原生HTML/CSS代码拼接各层元素
- 引入双重校验自修复机制：先做确定性布局规则检查（元素溢出、资源加载、DOM结构错误），再用VLM对比渲染结果与设计意图，生成局部代码补丁迭代修复
- 新增Agent Design Replay能力，序列化从需求拆解到代码修复的全决策轨迹，实现过程可追溯、可复现
### 关键实验
在海报、信息图、营销素材、长文本排版4类场景验证，对比纯扩散生成（GPT-Image-2）和纯代码生成（GPT-5.6 Sol驱动的Codex）两个baseline：纯扩散生成的中文文字错误率高，图层100%纠缠无法编辑；纯代码生成的设计布局单调，空白占比平均超30%；本方案在保持文字100%可编辑、图层完全解耦的基础上，美学评分与纯扩散方案持平，布局合规率达92%以上。
### 核心结论
把生成模型作为Agent可按需调用的外部模拟器与局部资产渲染器，让擅长推理的大模型做决策规划、擅长视觉的模型做内容生成，是兼顾效果与工程性的务实协作模式。
