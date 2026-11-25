---
title: 'AdProducer: Towards Agentic Advertising Video Generation'
title_zh: AdProducer：面向智能体的广告视频自动生成框架
authors:
- Kunyang Li
- Chaoyang Wang
- Mubarak Shah
- Yuzhang Shang
affiliations:
- University of Central Florida
arxiv_id: '2611.31466'
url: https://arxiv.org/abs/2611.31466
pdf_url: https://arxiv.org/pdf/2611.31466
published: '2026-11-22'
collected: '2026-11-25'
category: Agent
direction: 智能体广告生成 · 多模态工具调用
tags:
- Agent
- Multimodal
- Advertising Generation
- SFT
- RL
- Video Generation
one_liner: 提出端到端多模态智能体框架，冻结视频生成器即可大幅提升广告视频的准确性与传播效果
practical_value: '- 电商广告素材生成可复用「工具调用调研→卖点驱动分镜→冻结生成器渲染」的分层架构，无需微调视频生成器即可大幅降低产品幻觉，提升素材准确率

  - Agent 训练可借鉴 SFT + RL 联合分镜/视频双维度奖励的设计，避免生成器本身误差带来的奖励噪声，同时对齐创意设计与最终渲染效果

  - 广告类生成任务的评估可复用 PG-Score（产品正确性）+ Ad-Score（传播效果）的双维度评估体系，兼顾事实准确性和业务转化相关指标

  - 缺乏垂直领域训练数据时，可复用「大模型教师生成轨迹→多轮校验过滤」的数据集构建 Pipeline，快速产出 Agent 训练样本'
score: 10
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视频生成技术已支持高保真内容合成，但直接生成广告易出现产品属性错误、卖点展示缺失、事实幻觉等问题，无法满足广告对产品保真度和传播效果的双重要求；传统广告生产流程人工成本高、周期长，亟需自动化方案。
### 方法关键点
- 多模态Agent架构：集成文本搜索、网页浏览、图片搜索三类工具，自动完成产品事实校验、参考图收集，输出卖点驱动的镜头级分镜（含时长、运镜、文案、参考图绑定），输入给冻结的视频生成器渲染
- 两阶段训练：先在AdProducer-SFT数据集上做监督微调，模仿教师Agent的工具调用和分镜设计轨迹；再用GRPO做RL优化，联合分镜奖励（事实准确性、创意合理性）和视频奖励（最终渲染效果），α=0.5平衡两类权重
- 数据集与评估：构建4710条训练样本（3710条SFT、1000条RL），以及覆盖8个领域305条样本的AdCreation-Bench，提出PG-Score（产品正确性维度，权重：视觉正确性40%/文案准确率20%/卖点展示20%/分镜设计10%/美学10%）和Ad-Score（用户视角传播效果）双评估指标
### 关键结果
对接冻结MiniMax H3视频生成器，PG-Score从17.3提升至51.3，Ad-Score从2.72提升至4.70；无额外训练迁移到Veo 3.1，PG-Score从28.0提升至35.9，Ad-Score从2.87提升至3.47；人工评估显示产品保真度、信息丰富度、购买意愿均显著优于基线，同时VideoScore2通用视频质量指标不降反升。
> 最值得记住：垂直领域生成任务中，经过场景定制SFT+RL微调的小模型，效果远好于仅靠Prompt和工具调用的通用大模型
