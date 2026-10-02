---
title: 'Smaller Models, Better Rejects: Preference Distillation Scaling'
title_zh: 偏好蒸馏缩放：用更小模型生成更优DPO负样本
authors:
- Rui Cai
- Wenhui Zhu
- Xiwen Chen
- Jincheng Cao
- Han Yu
- Shayan Mohajer Hamidi
- Zelin He
- Qiyao Ma
- Daiwei Chen
- Xuanzhao Dong
affiliations:
- LinkedIn
- University of California, Davis
- Arizona State University
- Clemson University
- Pennsylvania State University
arxiv_id: '2609.38987'
url: https://arxiv.org/abs/2609.38987
pdf_url: https://arxiv.org/pdf/2609.38987
published: '2026-09-29'
collected: '2026-10-02'
category: Training
direction: LLM偏好蒸馏 · DPO负样本优化
tags:
- DPO
- Preference Distillation
- Knowledge Distillation
- Data Construction
- Low Cost Training
one_liner: 用远小于学生规模的冻结模型生成DPO负样本，降低成本同时提升偏好蒸馏效果
practical_value: '- 做业务侧LLM对齐（比如Agent工具调用、推荐文案/query生成的偏好优化）时，DPO负样本无需用同规模学生生成，直接用1B~3B级小模型即可获得更优效果，同时降低90%以上的负样本推理成本

  - DPO负样本不需要严格与prompt一一绑定，可提前构造小模型生成的领域负样本池跨prompt复用，大幅降低偏好训练的数据构造成本

  - 筛选DPO负样本时，优先选择在SeqKD参考模型下置信度低的样本，比选高置信度的近失样本可获得1%+的效果提升，且无需额外成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统偏好蒸馏默认采用学生模型自身生成的响应作为DPO负样本，隐含假设学生自身错误是最有信息量的对比负例；但随着学生模型规模从7B升至72B，负样本生成成本线性上涨，且学生生成的近失错误与参考政策耦合度高，可提供的对比价值有限，亟需低成本、高收益的负样本构造方案。

### 方法关键点
- 核心方案：采用规模远小于学生的冻结Base模型生成负样本，无需与学生同架构、同模型家族
- 三个可落地优化trick：混合负样本时提升小模型占比可线性提效、负样本可跨prompt重分配甚至仅保留任务相关词元结构仍有效、优先选择参考模型下置信度低的负样本
- 基于线性化DPO特征模型推导有限步效用边界，量化解释小模型负样本的增益来源

### 关键实验
在代码生成（KoDCode、HumanEval等）、数学推理（MATH-500、AIME）任务上，覆盖7B~72B全尺寸Qwen2.5学生模型，对比baseline为传统的学生自身负样本方案：
- 小模型负样本推理成本比同规模学生负样本低2x~108x，代码avg@4最高提升3.55个点，数学推理avg@4最高提升2.1个点
- 14B学生训练时，小模型负样本占比从0%升至100%，代码avg@4从59.73%线性升至63.28%
- 同候选池内选参考模型低置信度负样本，比高置信度方案在1.5B源上avg@4提升1.26个点

### 核心结论
DPO负样本只要保留任务结构且与参考政策耦合度低即可，无需跟随学生规模缩放，更小的冻结模型就能同时满足这两个要求且成本极低
