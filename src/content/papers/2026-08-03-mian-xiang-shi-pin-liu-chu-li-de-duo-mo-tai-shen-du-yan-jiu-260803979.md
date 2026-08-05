---
title: 'Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent'
title_zh: 面向视频流处理的多模态深度研究Agent框架Video-DeepResearch
authors:
- Zhen Fang
- Yu Zeng
- Wenxuan Huang
- Yiming Zhao
- Shiting Huang
- Tianfei Ren
- Qi Lu
- Qingnan Ren
- Qisheng Su
- Lionel Z. Wang
affiliations:
- USTC
- Xiaohongshu Inc.
- CUHK
- The Hong Kong Polytechnic University
- ZJU
arxiv_id: '2608.03979'
url: https://arxiv.org/abs/2608.03979
pdf_url: https://arxiv.org/pdf/2608.03979
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: 多模态Agent · 视频深度研究框架
tags:
- Multimodal Agent
- Video Understanding
- GRPO
- Tool Calling
- Benchmark
one_liner: 提出感知-探索解耦的分阶段工具解锁方案，35B视频研究Agent超Claude4.5 Sonnet 5个点
practical_value: '- 可借鉴分阶段工具解锁思路解决多模态Agent模态偏好问题：例如短视频商品理解Agent强制先做视频实体识别再调用文本检索，避免依赖参数记忆生成错误结果

  - SFT+GRPO两阶段训练范式可直接复用在工具调用类Agent训练上：先用标注的正确轨迹冷启动，再用RL优化自主探索能力，小参数模型也能追平大基线效果

  - 评测集构建的参数知识泄露过滤方法可迁移：先做无工具rollout筛掉模型靠记忆就能答对的样本，保证评测真实反映工具调用能力

  - 电商短视频/直播的商品识别、卖点挖掘场景可复用关键帧选择+实体裁剪搜索pipeline，提升多模态内容理解准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态深度研究Agent仅支持静态图像，直接迁移到视频流场景存在两个核心痛点：一是模态偏好，模型倾向于调用文本搜索而非视觉工具，二是参数知识泄露，依赖内部记忆而非真实工具调用完成任务，现有数据集和训练范式都不匹配视频场景的时空定位+跨模态探索需求。

### 方法关键点
- 数据层面：采用感知-探索解耦的轨迹生成pipeline，分阶段解锁工具：第一阶段仅开放Select_Keyframe、Crop_Search两类视觉工具，强制模型完成跨帧视觉定位后再开放Text_Search、页面访问等工具，共生成3万条视频VQA对和7千条高质量执行轨迹
- 训练层面：采用两阶段范式，先基于7k多模态轨迹+7k文本QA做SFT冷启动，再用GRPO做RL优化，强化自主探索能力
- 评测层面：构建VIDEODR-BENCH，包含200条多跳VQA样本，经过无工具rollout过滤，所有样本必须同时用到视觉搜索和外部知识推理才能解决

### 关键结果
在VIDEODR-BENCH上，35B版本模型准确率达64.0%，超Claude 4.5 Sonnet（59.0%）5个点，超GPT-5（52.5%）11.5个点；30B版本准确率达59.3%，和Claude 4.5 Sonnet持平，比同参数基线提升21.2%。工具调用统计显示训练后模型视觉工具调用量从单任务平均0.1次提升到2.33次，有效解决模态偏好问题。

### 核心结论
视频深度研究Agent的能力不是模型规模的副产物，而是需要专门的课程式训练设计引导模型学会先感知再检索的时序协作逻辑。
