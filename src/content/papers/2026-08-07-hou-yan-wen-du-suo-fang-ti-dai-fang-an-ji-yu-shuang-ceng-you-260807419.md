---
title: 'Beyond Post-Hoc Temperature Scaling: Bilevel Optimization for LLM Calibration'
title_zh: 后验温度缩放替代方案：基于双层优化的LLM校准方法
authors:
- Ruochen Jin
- Zhanliang Wang
- Zongyu Dai
- Jiancong Xiao
- Bojian Hou
affiliations:
- Dartmouth College
- University of Pennsylvania
- National University of Singapore
arxiv_id: '2608.07419'
url: https://arxiv.org/abs/2608.07419
pdf_url: https://arxiv.org/pdf/2608.07419
published: '2026-08-07'
collected: '2026-08-10'
category: LLM
direction: LLM校准 · 双层优化训练框架
tags:
- LLM Calibration
- Bilevel Optimization
- Temperature Scaling
- Entropy Maximization
- OOD Generalization
one_liner: 提出一阶近似双层优化训练时校准框架 解决后验温度缩放跨域泛化性差问题
practical_value: '- 做Agent/LLM驱动的推荐、智能客服、商品问答时，可复用CALM的熵最大化校准思路，缓解RLHF/DPO对齐后LLM过自信问题，减少错误回答的误导性，提升用户信任

  - 需要LLM跨域泛化的场景（比如跨品类的商品问答、多行业广告文案生成），优先用训练时校准方案替代后验温度缩放，避免每个域单独调温度的额外运维成本

  - 大模型微调时可复用论文的一阶近似双层优化实现方案，无需二阶计算，搭配QLoRA即可跑通，几乎不额外增加训练成本，性价比极高

  - 开放生成场景的校准效果评估可复用Sem-ECE指标，解决传统ECE无法适配无固定标签集的问题，更贴合电商开放问答、文案生成的实际评估需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RLHF/DPO等偏好对齐技术会让LLM出现严重过自信问题，传统后验温度缩放校准高度依赖域内数据集，跨域泛化性极差，无法满足通用LLM跨场景落地的校准需求，训练时校准是更优的解决方向。

### 方法关键点
- 采用双层优化框架：下层优化LLM参数保证任务性能，上层优化类温度超参数，以预测分布熵最大化为目标直接缓解过自信问题，无需额外标注
- 基于BOME算法做一阶近似优化，避免二阶导数和海森矩阵逆运算，适配百亿参数级大模型训练规模
- 采用QLoRA做参数高效微调，无需全量更新即可完成校准训练，工程实现门槛极低

### 关键结果
在4款经过RLHF/DPO对齐的开源模型（Llama-3.1-Tulu-8B、Vicuna-7B、Olmo 2-7B、Mistral-7B）上测试：跨域MCQA任务中CALM较基线最多降低41.1%的conf-ECE；开放生成跨域任务中较DPO基线降低20.7%的Sem-ECE，同时保留95%以上的原模型任务性能，远优于标签平滑、校准感知微调等基线。

**最值得记住的一句话**：后验温度缩放的跨域泛化缺陷可通过训练时引入熵最大化的双层优化解决，且几乎不会额外增加大模型微调的工程成本。
