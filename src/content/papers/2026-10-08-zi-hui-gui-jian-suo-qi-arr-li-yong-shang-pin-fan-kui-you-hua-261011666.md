---
title: 'Autoregressive Retriever: Improving Query Understanding from Item Feedback
  for Universal Multimodal Retrieval'
title_zh: 自回归检索器ARR：利用商品反馈优化通用多模态检索查询理解
authors:
- Jianfei Zhao
- Yifan Wang
- Feng Zhang
- Xin Sun
- Chong Feng
- Zhixing Tan
- Yang Luo
- Boyuan Pan
- Xu Kai
- Yao Hu
affiliations:
- Beijing Institute of Technology
- Zhongguancun Laboratory
- Xiaohongshu
- Southeast Academy of Information Technology, BIT
arxiv_id: '2610.11666'
url: https://arxiv.org/abs/2610.11666
pdf_url: https://arxiv.org/pdf/2610.11666
published: '2026-10-08'
collected: '2026-10-09'
category: RecSys
direction: 多模态检索 · 自回归反馈优化
tags:
- Multimodal Retrieval
- Query Understanding
- Relevance Feedback
- RL
- LoRA
- E-commerce Search
one_liner: 提出基于检索结果迭代优化查询嵌入的多模态检索框架ARR，保留预构建item索引复用能力
practical_value: '- 电商多模态搜索场景可直接复用ARR的迭代反馈架构：无需重训item索引，仅新增query端LoRA即可接入反馈优化，工程改造成本低

  - 训练流程可借鉴：先SFT用离线反馈池做步级对比学习加退化惩罚，再用GRPO做RL优化反馈item选择，兼顾收敛性与最终效果

  - 可复用结论：训练时加入反馈优化，即使推理时不开启迭代流程，初始query embedding性能也可提升0.4~0.8个百分点，无额外推理成本

  - 迭代次数可做成本收益折衷：实测2次迭代即可拿到80%以上的反馈增益，无需做到4次，大幅降低推理时延'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前通用多模态检索采用查询、item独立编码范式，查询嵌入生成后固定，无法利用检索结果消解歧义，存在查询-item语义鸿沟；现有反馈方法依赖额外改写模块，无法适配多模态输入，也无法端到端优化反馈item的选择。

### 方法关键点
- 自回归检索流程：迭代N次，每次基于当前查询嵌入检索Top1未选item，将其多模态内容拼入查询历史更新嵌入，最终用第N次嵌入做全库排序，item索引全程固定无需重建
- 两阶段训练：SFT阶段用预训练模型生成的离线反馈池采样轨迹，步级对比学习加退化惩罚（避免反馈后性能下降），仅初始步梯度回传item编码器；RL阶段冻结SFT主干和item索引，仅训练query端LoRA，用GRPO优化反馈item选择，奖励为最终正样本的 reciprocal rank，加低奖励轨迹的最终嵌入对比损失
- 推理可灵活开关迭代流程，兼容现有检索架构

### 关键结果
在M-BEIR 16个多模态任务、7个零样本基准上测试，对比TRACE、ELVA等SOTA基线；8B参数ARR-RL在M-BEIR平均得分61.0，超最强基线TRACE 2.2个百分点，零样本平均得分79.01，超基线ELVA 4.91个百分点；仅用反馈训练不开推理迭代，初始嵌入性能也比无反馈训练高0.4个百分点。

> 最值得记住的结论：基于检索结果的反馈优化不仅能提升迭代推理性能，还能反向增强初始查询嵌入的表征能力，额外训练成本低且可灵活开关推理流程
