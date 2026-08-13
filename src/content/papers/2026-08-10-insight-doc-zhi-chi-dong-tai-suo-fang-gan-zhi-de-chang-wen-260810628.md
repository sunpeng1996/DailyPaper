---
title: 'InSight-doc: Agentic Visual Perception for Long-Document Understanding'
title_zh: InSight-doc：支持动态缩放感知的长文档理解智能体框架
authors:
- Kaican Li
- Weiyan Xie
- Lewei Yao
- Jiannan Wu
- Lanqing Hong
- Yongxiang Huang
- Nevin L. Zhang
affiliations:
- The Hong Kong University of Science and Technology
- Huawei
arxiv_id: '2608.10628'
url: https://arxiv.org/abs/2608.10628
pdf_url: https://arxiv.org/pdf/2608.10628
published: '2026-08-10'
collected: '2026-08-12'
category: Agent
direction: 多模态智能体 · 长文档理解
tags:
- MLLM
- Agentic Perception
- Document VQA
- Long Context
- RL
- Multimodal
one_liner: 无外部检索器的自适应缩放多模态智能体，大幅提升长文档VQA精度同时降低推理成本
practical_value: '- 电商场景下处理多图商品详情页、多页资质文档、长说明书问答等多模态任务时，可复用「低分辨率全局输入+按需放大局部区域」的策略，大幅降低KV
  cache占用和推理延迟，避免全量高分辨率输入的成本问题

  - 训练支持动态工具调用的多模态Agent时，可参考「SFT先学习正确轨迹+RL优化策略效率」的两阶段训练范式，比直接给模型开放工具权限的效果提升显著，还能减少冗余调用

  - 多模态RAG场景可替代现有页级召回方案，采用区域级粒度的证据获取，既降低检索误差，又减少无关内容带来的token开销，适合商品图、详情页等布局复杂的内容理解'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长文档多模态理解面临两难：全量高分辨率输入会导致上下文腐烂、推理成本随序列长度平方级上升；依赖外部检索器的方案易引入检索误差，且只能做到页级粒度的召回，无法精准定位子页面关键信息，行业亟需平衡精度与效率的方案。

### 方法关键点
- 推理框架：初始输入低分辨率全量文档，智能体自主决策是否需要放大指定页面的指定区域，无外部检索器依赖，裁剪后的高分辨率区域直接追加到推理上下文，多轮迭代直到获得足够证据输出答案；
- 数据构造：三级过滤流程筛选需要动态缩放的样本，再通过双Agent（推理Agent+定位Agent）构造完整缩放轨迹，最终得到17.9K高质量SFT样本、19.2K难例RL样本；
- 训练范式：先通过SFT让模型学习缩放决策、区域定位和证据融合逻辑，再用GRPO RL算法优化策略，减少冗余调用、提升证据定位准确率。

### 关键结果
在4个长文档VQA基准（平均页数5.7~85.6页）上对比基线Qwen3-VL-8B：低初始分辨率下精度提升4.3~16.4个点，长文档场景幻觉率降低超40%，推理 latency 降低41%~68%，KV cache占用随序列长度降低最多达69%。

**最值得记住的结论**：将视觉分辨率作为推理时的动态可调资源，而非固定输入参数，是平衡长多模态任务精度与效率的核心思路。
