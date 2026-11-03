---
title: 'Reviso: Not All Visual Evidence Deserves Equal Attention in Video Captioning'
title_zh: Reviso：优先级引导主动感知的智能体视频字幕生成框架
authors:
- Tengfei Liu
- Yang Shi
- Yuran Wang
- Yuqi Tang
- Yizhuo Jia
- Zhuoran Zhang
- Qixun Wang
- Shujie Li
- Xuanyu Zhu
- Xinyu Liu
affiliations:
- PKU
- KlingAI Research
- HKUST(GZ)
- FDU
- THU
arxiv_id: '2611.03602'
url: https://arxiv.org/abs/2611.03602
pdf_url: https://arxiv.org/pdf/2611.03602
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: Agent 多模态视频字幕生成优化
tags:
- Video Captioning
- MLLM
- Active Perception
- GRPO
- Tool Use
one_liner: 提出分层观察规划与定制GRPO奖励的智能体视频字幕框架，性能优于现有开源基线
practical_value: '- 可复用CFP分层观察规划逻辑：电商短视频/直播内容理解场景中，先低帧率预览定场景（美妆/服饰/家电），再聚焦核心观察点（产品卖点、操作步骤），最后匹配工具（OCR读参数、放大看细节），大幅降低无效帧处理成本。

  - 定制化GRPO奖励设计可迁移：在基于Agent的商品信息提取、短视频内容审核任务中，同时设置核心信息准确率奖励、观察计划对齐奖励、无效工具调用惩罚，平衡效果与计算成本。

  - 验证引导的训练轨迹构建方法：缺乏高质量Agent执行轨迹时，可先由大模型生成候选轨迹，经事实验证+教师模型精修产出SFT训练数据，降低人工标注成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态大模型（MLLM）生成视频字幕时易过度关注次要细节，遗漏核心上下文与关键事件，均匀提升采样帧率不仅计算成本高，也无法保障关键信息覆盖，尤其在教程、广告、赛事等高信息密度场景下，字幕质量难以支撑下游视频理解任务。
### 方法关键点
- 分层Context-Focus-Points（CFP）观察规划：先低帧率采样得到全局预览，Context层识别视频场景与主活动，Focus层匹配场景优先级（如广告优先看产品参数、赛事优先看比分），Points层拆解为具体观察目标与对应工具（高帧率重访、裁剪、OCR）。
- 主动感知执行流程：按CFP规划多轮调用工具收集证据，动态更新未解决目标，最终融合全局上下文与局部证据生成字幕。
- 训练策略：先用验证引导pipeline构建高质量训练轨迹（大模型生成→事实验证→教师模型补全）做SFT，再用GRPO优化，奖励包含核心事实准确率奖励、观察计划对齐奖励、无效工具调用惩罚三类，平衡效果与成本。
### 关键结果
在4个视频字幕基准上对比15个开源MLLM基线，基于Qwen3.5-9B的Reviso：DREAM-1K F1较基线高4.4pp，MCTS-VCB F1高15.4pp，CaReBench动作F1、物体F1分别高9.1pp、6.7pp；下游视频QA任务LVBench准确率高4.9pp，MMVU整体准确率高2.1pp，为当前最优开源方案。
### 核心结论
不是所有视觉证据都值得同等关注，基于场景优先级的主动感知，比单纯提升采样帧率更能平衡效果与计算成本。
