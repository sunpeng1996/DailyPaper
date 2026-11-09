---
title: 'P^2-MOPD: Accelerating Multi-Teacher On-Policy Distillation via Parameter
  Priors'
title_zh: P²-MOPD：基于参数先验的多教师同策略蒸馏加速方法
authors:
- Sinuo Wang
- Jiacheng Lu
- Zeyu Zhang
- Maojia Song
- Rui Sun
- Beidi Luan
- Yutong Xie
- Jing Li
- Daxin Jiang
- Qi Wu
affiliations:
- Australian Institute for Machine Learning, Adelaide University
- StepFun
- Shanghai Jiao Tong University
- Singapore University of Technology and Design
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2611.03953'
url: https://arxiv.org/abs/2611.03953
pdf_url: https://arxiv.org/pdf/2611.03953
published: '2026-11-02'
collected: '2026-11-09'
category: Training
direction: 多教师同策略蒸馏 · 参数先验优化
tags:
- MOPD
- knowledge_distillation
- parameter_prior
- model_merging
- LLM_training
one_liner: 将专家参数作为可学习先验加入MOPD，减半训练步长同时提升能力均衡性
practical_value: '- 做跨领域电商/广告Agent基座蒸馏时，可直接复用该方法，相比传统MOPD训练周期减半，还能避免特定场景（如电商合规、金融营销）能力遗忘

  - 无需额外设计领域权重调度规则，靠蒸馏梯度自动调整各领域专家的贡献占比，省去了定期验证能力、手动合并欠拟合领域权重的人工成本

  - 工程改造量极小，仅新增少量混合系数参数，推理完全兼容原有模型结构，无需额外适配即可上线'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多教师同策略蒸馏（MOPD）是当前整合多个领域专家LLM能力的主流工业方案，广泛用于大模型多能力对齐，但存在两大痛点：一是训练成本极高，每步都需要采样学生轨迹并调用所有教师打标；二是领域能力不均衡，蒸馏过程易出现弱势领域能力被遗忘，即使从模型合并结果初始化也无法解决。而训练-free的模型合并方法虽然高效，但效果无法保证，平均仅能恢复不到一半的专家能力。
### 方法关键点
- 重参数化学生模型：将每个模块的权重表示为自身可训练全量权重 + 冻结领域专家任务向量的可学习线性组合，专家参数作为全程参数先验，不限制学生的参数空间范围
- 双通道联合优化：同一MOPD损失反向传播时，同时更新学生全量权重和混合系数，两个通道的梯度分开裁剪，互不占用预算
- 支持多粒度系数绑定：可选择模块/层/模型三种粒度的系数共享策略，无需额外验证信号，靠蒸馏梯度自动调整各领域的贡献比例
### 关键实验
基于Qwen3-1.7B和4B两个模型尺寸，覆盖医疗、法律、金融、指令跟随4个领域，对比MOPD、IM-MOPD、Open-MOPD等主流方案：
- 仅需一半训练步数即可超过MOPD的最终平均恢复率，训练总wall-clock仅比MOPD高9%~24%
- 1.7B模型最终平均恢复率达94.7%，远超MOPD的80.9%；最差领域恢复率从32%提升至88%，领域间能力标准差从28.4降至4.8
- 推理完全无开销，输出为标准模型 checkpoint，无需额外适配
### 核心结论
专家参数不需要仅作为初始化或单次合并的素材，全程作为可学习的参数先验参与蒸馏，可同时实现训练加速和跨领域能力均衡
