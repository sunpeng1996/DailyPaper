---
title: 'ERA: Entropy-Guided Visual Token Pruning with Rectified Attention for Efficient
  MLLMs'
title_zh: ERA：面向高效多模态大模型的熵引导视觉Token剪枝与注意力矫正
authors:
- Yuhao Wang
- Mu Qiao
- Haiwen Diao
- Yunzhi Zhuge
- Pingping Zhang
- Xindong Zhang
- Lei Zhang
- Huchuan Lu
affiliations:
- Dalian University of Technology
- Nanyang Technological University
- OPPO Research Institute
- The Hong Kong Polytechnic University
arxiv_id: '2606.31982'
url: https://arxiv.org/abs/2606.31982
pdf_url: https://arxiv.org/pdf/2606.31982
published: '2026-06-30'
collected: '2026-07-01'
category: Multimodal
direction: 多模态大模型 · 高效推理优化
tags:
- MLLM
- Visual Token Pruning
- Efficient Inference
- Attention Rectification
- Training-Free
one_liner: 提出免训练熵引导视觉Token剪枝框架，解决MLLM压缩后的注意力logit坍缩问题
practical_value: '- 多模态电商导购/商品理解场景可直接复用DEP剪枝逻辑，结合视觉多样性+注意力头熵筛选高价值视觉Token，高分辨率商品图、多图商品页场景下可压缩70%+视觉Token量，显著降低推理延时

  - BTR+LAR的注意力矫正方案可复用到所有Token剪枝/合并场景，无需修改FlashAttention等底层内核，仅通过矩阵扩增注入偏置即可解决logit坍缩问题，兼容现有推理部署框架

  - 直播/短视频商品理解、多图检索等长视觉上下文场景，该框架无需额外训练即可适配LLaVA、Qwen-VL等主流MLLM，极端压缩90%视觉Token仍保留90%以上性能，可直接集成到vLLM服务链路'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
MLLM推理时过长的视觉Token序列导致计算、KV Cache开销随分辨率/输入数量线性增长，现有免训练剪枝/合并方法会引发**注意力Logit坍缩**：剪枝后视觉Token的注意力占比从全量的61%骤降到18%，注意力过度偏移到系统、指令Token，高分辨率图、多图、视频场景下性能损失严重。
### 方法关键点
- 双视角熵剪枝（DEP）：拼接视觉特征与注意力头熵特征，通过熵惩罚的贪心搜索选择锚点Token，同时覆盖视觉内容多样性与头级显著性
- 偏置感知Token回收（BTR）：将剪去的Token合并到最近锚点，基于每个Token的熵值计算聚类级logit偏置，保留剪去Token的注意力贡献
- 保Logit注意力矫正（LAR）：将聚类偏置以对数项形式注入注意力计算，通过矩阵扩增实现，完全兼容FlashAttention等优化内核，无需修改底层实现
### 关键结果
在LLaVA-1.5、LLaVA-NeXT、Qwen2.5-VL、InternVL3等主流MLLM上测试，极端压缩94%视觉Token时仍保留93%~96%的全量性能，比SOTA剪枝方法平均高1~2pp；LLaVA-NeXT-7B压缩到160个Token后，Prefill速度提升4.5倍，KV Cache占用从1.44GB降到0.08GB，端到端延时从544ms降到200ms，无明显性能损失。
> 最值得记住：免训练视觉Token剪枝的核心瓶颈不是选Token的策略，而是剪枝后如何矫正被系统性低估的视觉注意力logit
