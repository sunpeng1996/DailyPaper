---
title: 'Beyond PINNs: A Unified Gauss--Newton and Petrov--Galerkin Framework for Neural
  and Hybrid PDE Solvers'
title_zh: 超越PINNs：面向神经与混合PDE求解器的高斯牛顿-彼得罗夫伽辽金统一框架
authors:
- Nilo Schwencke
- Roland Maier
arxiv_id: '2609.20641'
url: https://arxiv.org/abs/2609.20641
pdf_url: https://arxiv.org/pdf/2609.20641
published: '2026-09-17'
collected: '2026-09-21'
category: Other
direction: PDE数值求解 · 神经有限元混合框架
tags:
- PINNs
- PDE Solver
- Gauss-Newton
- Petrov-Galerkin
- Hybrid Solver
one_liner: 提出统一高斯牛顿与Petrov-Galerkin的框架，覆盖PINNs与有限元两类PDE求解范式
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前物理 informed 神经网络（PINNs）与有限元是两类主流PDE求解范式，前者基于逐点强残差最小化训练，后者基于弱变分离散构建，二者缺乏统一理论框架，难以支撑跨范式算法设计。
### 方法关键点
1. 提出基于线性测量族离散泛函高斯牛顿问题的统一框架，通过对偶配对将线性测量映射为测试函数，所得高斯牛顿系统等价于线性化泛函问题的Petrov-Galerkin离散；
2. 可自然覆盖点配置、自然梯度构造等现有方法作为特例，将测试函数选择明确为可调控的算法设计变量；
3. 针对椭圆PDE问题可衍生出弱残差公式、有限元-神经混合构造，作用于互补近似空间提升求解能力。
### 关键结果
数值实验验证了框架的正确性，弱高斯牛顿公式、有限元-神经混合近似的求解效果显著优于传统PINNs与有限元基线。
