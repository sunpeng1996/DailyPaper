---
title: 'R$^2$-Omni: Reducing Structural and Precision Redundancy in Omni-LLMs for
  Long-Form Generation'
title_zh: R²-Omni：面向多模态大模型长生成的双重冗余压缩框架
authors:
- Bolong Feng
- Pengfei Zhou
- Zhenglin Wan
- Wei Wang
- Wangbo Zhao
affiliations:
- InfRec, Cardinal AI Lab
- Shanghai Jiao Tong University
- National University of Singapore
- The Hong Kong University of Science and Technology
arxiv_id: '2611.03247'
url: https://arxiv.org/abs/2611.03247
pdf_url: https://arxiv.org/pdf/2611.03247
published: '2026-11-02'
collected: '2026-11-03'
category: LLM
direction: 多模态大模型 · KV cache 推理优化
tags:
- KV-cache
- Quantization
- Token Pruning
- Multimodal LLM
- Long-Context Inference
one_liner: 训练免精调框架联合压缩多模态token与KV缓存冗余，长生成场景下5倍降内存保98%性能
practical_value: '- 长视频/直播理解场景可直接复用STC模块：基于视频时空相似性、音频局部连续性合并冗余token，无需训练就能降低多模态输入长度，比query引导的剪枝更能保留生成所需细节，适合直播内容总结、商品视频文案生成等长生成任务

  - KV cache量化可借鉴SSPA的语义敏感分配策略：结合query注意力分数+音视频对齐信号做语义先验，给高语义价值token分配更高精度，在相同内存预算下能减少生成质量损失，可迁移到图文/多模态推荐的LLM推理服务降本

  - 训练免精调的联合压缩架构可直接落地：不需要修改模型权重，仅在推理前处理和KV缓存阶段插入两个模块，适配不同多模态大模型，适合业务侧快速上线降本，不用重新训练大模型

  - 性能结论可直接参考：5倍KV压缩下保留97.98%生成质量，1.48倍端到端提速，9倍压缩下仍保留95%以上质量，可作为多模态LLM推理服务资源规划的参考指标'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有多模态大模型处理长音视频输入时，大量多模态token会大幅提升prefill计算量与KV cache内存占用；传统query引导的token剪枝在多选任务上表现优异，但长开放生成场景下会丢弃大量非query相关的细粒度信息，生成质量下降严重；仅做KV cache量化无法利用token层面的结构冗余，压缩效率存在明显瓶颈。
### 方法关键点
- 训练免精调两阶段压缩框架，无需修改模型权重即可快速适配不同多模态大模型
- 结构感知Token合并（STC）：视频基于帧内空间相似性、帧间时间相似性合并冗余视觉token，音频基于局部连续性合并相邻相似音频token，不依赖query注意力排序，避免丢失生成所需的细节信息
- 语义敏感精度分配（SSPA）：将保留的token按32个为单位划分为page，结合query注意力分数、音视频对齐信号生成语义先验，以最小化注意力输出误差为目标，给不同page分配INT2/INT4/BF16精度，进一步降低KV cache内存占用
### 关键结果
在Video-SALMONN2、LongVALE、OmniDCBench三个长生成基准，Qwen2.5-Omni 3B/7B、MiniCPM-o-4.5三个多模态大模型上测试，对比OmniZip、KIVI等6种剪枝/量化基线：平均实现5.0×KV内存压缩，保留97.98%的基线生成质量，端到端推理提速1.48×；9倍压缩下仍保留95.21%的生成质量，效果大幅优于token剪枝+KV量化的朴素组合方案。
### 核心结论
长开放生成场景下，联合压缩token结构冗余与KV精度冗余，比单纯剪枝或单纯量化能在更高压缩率下保留更多细粒度语义信息。
