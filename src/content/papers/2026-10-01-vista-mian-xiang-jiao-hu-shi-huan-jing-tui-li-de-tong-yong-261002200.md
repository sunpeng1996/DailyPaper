---
title: 'VISTA: A Visual Harness for Reasoning in an Interactive World'
title_zh: VISTA：面向交互式环境推理的通用视觉管控框架
authors:
- Qiushi Han
- Keya Hu
- Linlu Qiu
- Cathy Wu
- Kaiming He
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2610.02200'
url: https://arxiv.org/abs/2610.02200
pdf_url: https://arxiv.org/pdf/2610.02200
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: 多模态Agent · 视觉推理与环境交互
tags:
- Multimodal Agent
- Visual Reasoning
- Memory System
- Tool Use
- Interactive Environment
one_liner: 通过无损视觉记忆与主动检索工具链释放多模态模型的长周期视觉推理能力
practical_value: '- 开发电商导购Agent、直播间自动运营Agent、广告投放自动化Agent时，可复用无损视觉记忆模块：存储全分辨率交互历史帧，支持按时间/空间区域检索，避免重复识别错误，同时降低token开销

  - 做GUI交互类Agent时，可给VLM增加主动inspect工具，让模型自主决定是否放大局部区域、读取像素值，避免低分辨率截图漏细节导致的操作错误，比全量传高清图省70%以上token

  - 长周期交互任务无需盲目堆大上下文窗口，可搭配GUIDE.md（全局规则）+ WORKING.md（当前任务草稿）的双笔记机制，上下文满时仅保留核心笔记和当前状态，token开销降50%的情况下性能损失不到0.5%'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多模态Agent做长周期交互时，视觉观测仅编码一次，压缩后的表示易丢失后续推理需要的细节，且上下文窗口限制导致历史观测被丢弃或仅保留文本摘要，严重限制复杂交互式环境下的推理能力；现有ARC-AGI-3等基准的方案大多依赖程序合成，泛化到复杂视觉场景的难度极高。

### 方法关键点
- 视觉观测：直接向模型输出环境渲染的全分辨率图像，保留物体外观与空间关系，避免文本/符号表示的信息损失
- 无损视觉记忆：存储所有交互返回的原始帧（含动画中间帧），按回合+帧号索引，不受模型上下文窗口限制
- 主动视觉检索工具：支持模型自主调用inspect工具，跨时间检索任意历史帧、放大指定空间区域，还支持读取指定区域像素值，所有检索操作不占用交互动作配额
- 双笔记机制：支持模型维护GUIDE.md（存储跨关卡通用规则）和WORKING.md（当前任务草稿），上下文满时仅保留核心笔记和当前状态，截断后无缝继续

### 关键实验
在ARC-AGI-3的25个公开交互游戏上，Claude Opus 5.0的RHAE得分从官方基线的40.68提升到满分100，动作数比首次参与的人类玩家少57.4%；GPT-5.6 Sol得分从13.33提升到99.00。用图像观测比传统文本网格表示省57%的token，动作数还少14%。在GameWorld上任务成功率比基线高23.3%，超过新手人类玩家水平；AI GameStore上得分是人类中位数的1.4倍；BabyVision准确率从41%提升到63.2%。

最值得记住的一句话：好的harness设计对释放大模型已有能力的价值，不亚于模型本身的性能提升
