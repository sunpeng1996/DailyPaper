---
title: 'What to Edit Next: Visually Aligned Image-Editing Follow-Up Suggestions in
  Conversational Systems'
title_zh: 对话系统中视觉对齐的图像编辑后续操作推荐方法
authors:
- Zhijing Zhang
- Jinpeng Yu
- Xin Song
- Bingnan Li
- Chuyue Li
- Changhui Du
- Xiaolin Fang
- Jiaming Liu
- Ruihua Huang
affiliations:
- Alibaba Qwen Business Unit
- Southeast University
arxiv_id: '2608.07565'
url: https://arxiv.org/abs/2608.07565
pdf_url: https://arxiv.org/pdf/2608.07565
published: '2026-08-02'
collected: '2026-08-11'
category: QueryRec
direction: 多模态查询推荐 · 视觉对齐优化
tags:
- Multimodal Recommendation
- Query Suggestion
- GRPO
- Visual Grounding
- RLHF
- Industrial Application
one_liner: 提出三阶段训练框架，结合人工意图、点击偏好RL与视觉校验，优化对话式图像编辑后续推荐效果
practical_value: '- 对话式多模态Query推荐场景（如电商AI作图工具后续编辑建议、商品修图助手）可复用三阶段范式：先人工定义合法意图空间做SFT冷启动，再用点击反馈做RL对齐偏好，最后加模态一致性校验避免幻觉

  - 处理点击偏好的位置bias时，可直接复用「仅将点击项与上方展示的未点击项配对」的轻量化策略，无需复杂的倾向得分估计即可有效降低位置偏差，提升奖励模型准确率

  - 多目标GRPO优化时，对输出格式、内容长度、多样性等硬约束类指标采用动态权重调整机制：指标不达标时自动升权，达标时降权，平衡业务约束与用户偏好目标，避免过优化

  - 多模态场景的幻觉校验可借鉴source-target拆分逻辑：先观察图像记录当前状态，再拆分query的前置依赖和目标状态分别校验，相比单端VLM直接打分准确率更高、误判率更低，且仅在训练阶段使用不增加推理延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有对话系统的后续推荐多面向纯文本场景，图像创作类对话的后续编辑推荐能力缺失。对10万条通义千问App真实多轮作图对话的审计显示，80.1%的后续编辑请求依赖图像上下文，仅靠文本上下文无法推导，现有方案要么仅对齐用户点击偏好，要么不校验编辑操作的视觉可行性，导致推荐的编辑指令无法执行、用户留存低。

### 方法关键点
- 三阶段训练框架：Stage1 基于真实在线上下文+人工审核的61种后续编辑意图表，生成校验后的SFT数据集，用LoRA微调Qwen3-VL-8B基线模型，冷启动推荐能力；
- Stage2 构造位置感知的点击对（仅将点击项与上方未点击项配对）训练8B多模态奖励模型，通过多目标GRPO优化点击偏好、输出合法性、与SFT分布的PPL相似度、内容感知长度、列表内多样性共5个奖励，对齐用户真实选择；
- Stage3 新增图像优先的source-target视觉校验器：先记录图像当前状态，拆分每个编辑建议的必需前置源和目标状态，分别校验源是否存在、目标是否已满足，将一致性得分作为第6个奖励加入GRPO优化，仅在训练阶段使用。

### 关键结果
离线评估中，完整框架将视觉不一致率从Stage2的3.7%降至0.9%；在通义千问App百万级用户的14天A/B测试中，对比prompt工程基线，推荐CTR提升32.70%，图像保存率提升16.32%，用户平均对话轮次提升39.90%，所有提升均统计显著（p<0.05）。

**最值得记住的一句话**：多模态生成式推荐不能只对齐用户行为偏好，必须补充模态原生的一致性校验信号，才能兼顾点击转化和长期用户体验。
