---
title: 'Complex KDA: Understanding and Enhancing the Expressivity of Kimi Delta Attention'
title_zh: Complex KDA：提升Kimi Delta Attention的表达能力
authors:
- Julien Siems
- Riccardo Grazzi
- Korbinian Pöppel
- Jaisidh Singh
- Arber Zela
- Timur Carstensen
- Jenia Jitsev
- Frank Hutter
- Volkan Cevher
- Antonio Orvieto
affiliations:
- University of Freiburg
- Microsoft Research
- University of Tübingen
- MPI-IS Tübingen
- EPFL
arxiv_id: '2609.24797'
url: https://arxiv.org/abs/2609.24797
pdf_url: https://arxiv.org/pdf/2609.24797
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: 线性RNN · KDA架构优化
tags:
- Linear RNN
- Kimi Delta Attention
- Sequence Modeling
- LLM Backbone
- Long Sequence
one_liner: 通过扩展KDA参数范围实现平面旋转，在保留效率的同时大幅提升线性RNN的状态追踪能力
practical_value: '- 长序列用户行为建模场景可直接借鉴CKDA的参数扩展思路，将delta系数β设为[0,2]、通道门限范围扩展到[-1,1]，几乎不损失推理速度的前提下，提升用户复购周期、大促行为等周期性规律的建模效果

  - 自研LLM作为推荐/Agent底座的团队可复用CKDA的工程实现，仅需修改KDA少量内核代码，即可保留96~97%的原始KDA吞吐量，同时获得更优的长序列外推能力

  - 用户未来行为序列预测、复购时间预测等生成类推荐场景，可引入CKDA的旋转建模机制，解决传统Transformer长序列预测的相位丢失问题，提升周期性行为预测准确率'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
基于delta规则的线性RNN（如KDA）具备序列长度线性复杂度的高效推理能力，但低秩校正的线性更新限制了表达能力，此前实现2D旋转需堆叠2次delta规则转换，会显著提升计算成本；KDA原生的通道级门控具备低成本实现旋转的潜力，但原有参数范围约束了该能力的释放。
### 方法关键点
- 提出Complex KDA（CKDA），同时扩展两个核心参数范围：通道门限α从[0,1]扩展至[-1,1]，delta规则系数β从[0,1]扩展至[0,2]
- 理论证明该结构可在单次循环更新内实现任意2D旋转，过渡矩阵仍保持对角加秩一结构，保留原有稳定性与计算效率
- 理论上证明所有正交对角加秩一矩阵均可表示为CKDA过渡矩阵，单CKDA层可追踪所有SO(3)子群同构的有限群，比同类线性RNN少用1层
### 关键实验结果
- 状态追踪任务：S3、S4长序列外推任务上，序列长度扩展到512时CKDA仍保持接近满分的准确率，其他KDA变体准确率不足0.2
- 周期音频续接任务：训练长度136，外推到264时CKDA SNR达38.1dB，远高于普通Transformer的2.8dB
- 1.3B参数LLM训练100B token，CKDA下游任务平均准确率达54.06%，与KDA持平，优于Mamba-3、Transformer等基线，吞吐量保留原始KDA的96~97%

> 最值得记住的结论：仅扩展KDA的两个参数范围，即可在几乎无效率损失的前提下大幅提升线性RNN的长序列周期建模能力，是现有KDA架构的零成本升级方案
