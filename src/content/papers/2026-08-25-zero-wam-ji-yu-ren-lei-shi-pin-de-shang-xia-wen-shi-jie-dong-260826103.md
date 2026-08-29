---
title: 'Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended
  Task Generalization'
title_zh: Zero-WAM：基于人类视频的上下文世界动作建模实现开放任务泛化
authors:
- Jiaming Zhou
- Qihang Zhang
- Gangwei Xu
- Cunxin Fan
- Yujie Zhao
- Ruilin Wang
- Yiming Luo
- Shuai Yang
- Xing Zhu
- Yujun Shen
affiliations:
- Robbyant
- HKUST (GZ)
- HKUST
arxiv_id: '2608.26103'
url: https://arxiv.org/abs/2608.26103
pdf_url: https://arxiv.org/pdf/2608.26103
published: '2026-08-25'
collected: '2026-08-29'
category: Other
direction: 机器人学习 · 零样本跨任务泛化
tags:
- In-Context Learning
- Zero-Shot Generalization
- Video Prompt
- Robot Learning
- Training Objective
one_liner: 提出基于人类视频prompt的机器人ICL框架Zero-WAM，大幅提升零样本跨操作任务泛化能力
practical_value: '- 针对推荐/广告系统冷启动泛化需求，可复用IFP训练目标思路，设计损失函数抑制模型在历史热门数据上的捷径学习，强制模型从prompt中抽取新场景/新物品的核心特征

  - 缺乏跨域配对标注数据时，可借鉴自动生成配对数据集的pipeline，比如将用户行为轨迹自动匹配对应语义的文案/视频样本，大幅降低标注成本

  - 多模态Agent任务调度时，可优先选择包含更丰富时序/空间信息的视频作为prompt输入，比纯文本指令的跨场景泛化效果更稳定'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
机器人学习领域零样本跨任务泛化是核心难题，现有ICL范式多依赖文本指令，无法提供操作任务所需的丰富视觉演化线索，同时跨任务人-机器人配对训练数据极度稀缺。
### 方法关键点
1. 构建Zero-WAM因果视频-动作模型，支持直接以人类视频作为上下文prompt，无需参数更新即可执行未见过的操作任务
2. 提出自动数据生成pipeline，将采样的机器人轨迹匹配生成语义对应的人类视频，产出包含8.6K任务、74.2K人-机器人ICL配对的HumanGen数据集
3. 设计上下文未来块预测（IFP）训练目标，抑制模型从已见任务学到的捷径，强制其从视频prompt中抽取核心任务信息
### 关键结果
RoboTwin 2.0仿真环境7个未见任务上平均成功率达47.0%，较最强视频-动作基线绝对提升29.5个百分点；真实环境下可泛化到多物体场景、长时序操作、精细插入等未见任务配置。
